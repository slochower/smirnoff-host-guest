#!/usr/bin/env python
"""
Provides a wrapper script to convert a given host-guest system to SMIRNOFF parameters.
"""

from .utils import *
from openforcefield.typing.engines.smirnoff import ForceField, unit
from openforcefield.utils import mergeStructure

import parmed as pmd
import glob


def convert(destination,
            prefix,
            reference_prmtop,
            reference_inpcrd,
            host_resname,
            guest_resname,
            debug=False):
    """
    Convert from an existing parameter set to SMIRNOFF99Frosst.
    Parameters
    ----------
    destination : str
        Directory where existing files will be read and new files will be written
    prefix : str
        Base name of output files (e.g., "smirnoff" or "hg")
    reference_prmtop : str
        Name of existing AMBER parameter file
    reference_inpcrd : str
        Name of existing AMBER coordinate file
    host_resname : str
        Residue name of the host molecule (*not* the mask)
    guest_resname : str
        Residue name of the guest molecule (*not* the mask)
    debug : bool
        If True, intermediary files will be kept

    Returns
    -------
    merged : parmed.Structure
        A ParmEd structure containing the SMIRNOFF99Frosst parameters and coordinates
    """

    clean_up(
        destination=destination,
        host_resname=host_resname,
        guest_resname=guest_resname)
    reference = pmd.load_file(
        destination + reference_prmtop, xyz=destination + reference_inpcrd)

    create_pdb_with_conect(
        solvated_pdb=destination + reference_inpcrd,
        amber_prmtop=destination + reference_prmtop,
        output_pdb=destination + prefix + '.pdb')

    prune_conect(
        input_pdb=prefix + '.pdb',
        output_pdb=prefix + '.pruned.pdb',
        path=destination)

    components = split_topology(file_name=destination + prefix + '.pruned.pdb')
    hg_topology = create_host_guest_topology(
        components, host_resname=host_resname, guest_resname=guest_resname)

    create_host_mol2(
        solvated_pdb=destination + prefix + '.pruned.pdb',
        amber_prmtop=destination + reference_prmtop,
        mask=host_resname,
        output_mol2=destination + host_resname + '.mol2')

    create_host_mol2(
        solvated_pdb=destination + prefix + '.pdb',
        amber_prmtop=destination + reference_prmtop,
        mask=guest_resname,
        output_mol2=destination + guest_resname + '.mol2')

    convert_mol2_to_sybyl_antechamber(
        input_mol2=destination + host_resname + '.mol2',
        output_mol2=destination + host_resname + '-sybyl.mol2',
        ac_doctor=False)

    convert_mol2_to_sybyl_antechamber(
        input_mol2=destination + guest_resname + '.mol2',
        output_mol2=destination + guest_resname + '-sybyl.mol2',
        ac_doctor=False)

    extract_water_and_ions(
        amber_prmtop=reference_prmtop,
        amber_inpcrd=reference_inpcrd,
        host_residue=':' + host_resname,
        guest_residue=':' + guest_resname,
        dummy_atoms=True,
        output_pdb='water_ions.pdb',
        path=destination)

    create_water_and_ions_parameters(
        input_pdb='water_ions.pdb',
        output_prmtop='water_ions.prmtop',
        output_inpcrd='water_ions.inpcrd',
        dummy_atoms=False,
        path=destination)

    host = load_mol2(
        filename=destination + host_resname + '-sybyl.mol2',
        name=host_resname,
        add_tripos=True)

    guest = load_mol2(
        filename=destination + guest_resname + '-sybyl.mol2',
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
        hg_structure.save(destination + 'hg.prmtop')
    except OSError:
        print('Check if the host-guest parameter file already exists...')

    try:
        hg_structure.save(destination + 'hg.inpcrd')
    except OSError:
        print('Check if the host-guest coordinate file already exists...')

    water_and_ions = pmd.amber.AmberParm(
        destination + 'water_ions.prmtop',
        xyz=destination + 'water_ions.inpcrd')

    merged = mergeStructure(hg_structure, water_and_ions)
    merged.box = reference.box
    try:
        merged.save(destination + 'smirnoff.prmtop')
    except:
        print('Check if solvated parameter file already exists...')
    try:
        merged.save(destination + 'smirnoff.inpcrd')
    except:
        print('Check if solvated coordinate file already exists...')

    if not debug:
        clean_up(
            destination=destination,
            host_resname=host_resname,
            guest_resname=guest_resname)

    return merged


def clean_up(destination, host_resname, guest_resname):
    """
    Clean up intermediary files created during the conversion.
    Parameters
    ----------
    destination : str
        Path of the intermediate files
    host_resname : str
        Residue name of the host molecule
    guest_resname : str
        Residue name of the guest molecule


    """
    water = glob.glob(destination + 'water_ions*')
    host = glob.glob(destination + host_resname + '*')
    guest = glob.glob(destination + guest_resname + '*')
    for file in water + host + guest:
        try:
            print(f'Removing {file}...')
            os.remove(destination + file)
        except:
            pass