import numpy as np
import subprocess as sp
import os as os

from openeye.oechem import *
from openforcefield.typing.engines.smirnoff import *
from openforcefield.utils import mergeStructure
import parmed as pmd

from utils import create_pdb_with_conect, prune_conect
from utils import split_topology, create_host_guest_topology
from utils import create_host_mol2, convert_mol2_to_sybyl_antechamber
from utils import load_mol2, check_unique_atom_names, load_pdb
from utils import extract_water_and_ions, create_water_and_ions_parameters
from utils import check_bond_lengths
from utils import extract_dummy_atoms, create_dummy_atom_parameters
from utils import map_residues, map_atoms
from utils import copy_box_vectors
from utils import rewrite_restraints_file, rewrite_amber_input_file
from utils import color_restraints


def convert_parameters(source_directory='original/',
                       source_crd='full.crds',
                       source_top='full.topo',
                       destination_directory='generated/',
                       destination_crd='smirnoff.inpcrd',
                       destination_top='smirnoff.prmtop',
                       host_resname='MGO',
                       guest_resname='BAM'):

    create_pdb_with_conect(
        solvated_pdb=source_directory + source_crd,
        amber_prmtop=source_directory + source_top,
        output_pdb=destination_directory + 'full.pdb')

    prune_conect(
        input_pdb='full.pdb',
        output_pdb='full_conect.pdb',
        path=destination_directory)

    components = split_topology(file_name=destination_directory + 'full.pdb')
    hg_topology = create_host_guest_topology(
        components, host_resname=host_resname, guest_resname=guest_resname)

    create_host_mol2(
        solvated_pdb=destination_directory + 'full.pdb',
        amber_prmtop=source_directory + source_top,
        mask=host_resname,
        output_mol2=destination_directory + host_resname + '.mol2')

    convert_mol2_to_sybyl_antechamber(
        input_mol2=destination_directory + host_resname + '.mol2',
        output_mol2=destination_directory + host_resname + '-sybyl.mol2',
        ac_doctor=True)

    host = load_mol2(
        filename=destination_directory + host_resname + '-sybyl.mol2',
        name=host_resname,
        add_tripos=True)
    guest = load_mol2(
        filename=source_directory + guest_resname.lower() + '.mol2',
        name=guest_resname,
        add_tripos=False)
    check_unique_atom_names(host)
    check_unique_atom_names(guest)
    molecules = [host, guest]

    ff = ForceField('forcefield/smirnoff99Frosst.ffxml')
    system = ff.createSystem(
        hg_topology.topology,
        molecules,
        nonbondedCutoff=1.1 * unit.nanometer,
        ewaldErrorTolerance=1e-4)

    hg_structure = pmd.openmm.topsystem.load_topology(
        hg_topology.topology, system, hg_topology.positions)

    check_bond_lengths(hg_structure, threshold=4)

    try:
        hg_structure.save(destination_directory + 'hg.prmtop')
    except OSError:
        print('Check if the host-guest parameter file already exists...')

    try:
        hg_structure.save(destination_directory + 'hg.inpcrd')
    except OSError:
        print('Check if the host-guest coordinate file already exists...')

    extract_water_and_ions(
        amber_prmtop=source_directory + source_top,
        amber_inpcrd=source_directory + source_crd,
        host_residue=':' + host_resname,
        guest_residue=':' + guest_resname,
        dummy=None,
        output_pdb=destination_directory + 'water_ions.pdb')

    create_water_and_ions_parameters(
        input_pdb='water_ions.pdb',
        output_prmtop='water_ions.prmtop',
        output_inpcrd='water_ions.inpcrd',
        dummy_atoms=True,
        path=destination_directory)

    water_and_ions = pmd.amber.AmberParm(
        destination_directory + 'water_ions.prmtop',
        xyz=destination_directory + 'water_ions.inpcrd')

    merged = mergeStructure(hg_structure, water_and_ions)

    try:
        merged.save(destination_directory + destination_top)
    except:
        print('Check if solvated parameter file already exists...')
    try:
        merged.save(destination_directory + destination_crd)
    except:
        print('Check if solvated coordinate file already exists...')

    reference = pmd.load_file(source_directory + source_top,
                              source_directory + source_crd)
    try:
        reference.save(destination_directory + 'reference.pdb')
        reference.save(destination_directory + 'reference.mol2')
    except OSError:
        print('Check if file exists...')
    target = pmd.load_file(destination_directory + destination_top,
                           destination_directory + destination_crd)
    try:
        target.save(destination_directory + 'target.pdb')
        target.save(destination_directory + 'target.mol2')
    except OSError:
        print('Check if file exists...')

    reference_mol = load_mol2(destination_directory + 'reference.mol2')
    target_mol = load_mol2(destination_directory + 'target.mol2')

    atom_mapping = map_atoms(reference_mol, target_mol)

    reference_mol = load_pdb(destination_directory + 'reference.pdb')
    target_mol = load_pdb(destination_directory + 'target.pdb')

    residue_mapping = map_residues(atom_mapping, reference_mol, target_mol)

    for file in ['mini.in', 'therm1.in', 'therm2.in', 'eqnpt.in', 'mdin']:
        rewrite_amber_input_file(
            reference_input=source_directory + file,
            target_input=destination_directory + file,
            reference_to_target_mapping=residue_mapping,
            dt_override=True)

    rewrite_restraints_file(
        reference_restraints=source_directory + 'disang.rest',
        target_restraints=destination_directory + 'disang.rest',
        reference_to_target_mapping=atom_mapping)

    # copy_box_vectors(
    #     input_inpcrd=source_directory + source_crd,
    #     output_inpcrd=destination_directory + destination_crd)

    # For some reason, this must come last, otherwise it gets removed again
    merged.box = reference.box
    try:
        os.remove(destination_directory + destination_top)
        os.remove(destination_directory + destination_crd)
    except OSError:
        pass
    merged.save(destination_directory + destination_crd)
    merged.save(destination_directory + destination_top)