#!/usr/bin/env python
"""
Provides a wrapper script to convert a given host-guest system to SMIRNOFF parameters.
"""

from .utils import *
from openforcefield.typing.engines.smirnoff import ForceField, unit
from openforcefield.utils import mergeStructure

import parmed as pmd
import glob
import os


def convert(
    source,
    destination,
    prefix,
    reference_prmtop,
    reference_inpcrd,
    host_resname,
    guest_resname,
    dummy=False,
    debug=False,
):
    """
    Convert from an existing parameter set to SMIRNOFF99Frosst.
    Parameters
    ----------
    source : str
        Directory where existing files will be read
    destination : str
        Directory where new files will be written
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
    dummy : bool
        Whether the reference structures include dummy atoms
    debug : bool
        If True, intermediary files will be kept

    Returns
    -------
    merged : parmed.Structure
        A ParmEd structure containing the SMIRNOFF99Frosst parameters and coordinates
    """

    clean_up(
        destination=destination, host_resname=host_resname, guest_resname=guest_resname
    )
    reference = pmd.load_file(
        os.path.join(source, reference_prmtop),
        xyz=os.path.join(source, reference_inpcrd),
    )

    create_pdb_with_conect(
        solvated_pdb=os.path.join(source, reference_inpcrd),
        amber_prmtop=os.path.join(source, reference_prmtop),
        output_pdb=os.path.join(destination, prefix) + ".pdb",
    )

    prune_conect(
        input_pdb=prefix + ".pdb", output_pdb=prefix + ".pruned.pdb", path=destination
    )

    components = split_topology(
        file_name=os.path.join(destination, prefix) + ".pruned.pdb"
    )
    hg_topology = create_host_guest_topology(
        components, host_resname=host_resname, guest_resname=guest_resname
    )

    create_host_mol2(
        solvated_pdb=os.path.join(destination, prefix) + ".pruned.pdb",
        amber_prmtop=os.path.join(source, reference_prmtop),
        mask=host_resname.upper(),
        output_mol2=os.path.join(destination, host_resname) + ".mol2",
    )

    create_host_mol2(
        solvated_pdb=os.path.join(destination, prefix) + ".pdb",
        amber_prmtop=os.path.join(source, reference_prmtop),
        mask=guest_resname.upper(),
        output_mol2=os.path.join(destination, guest_resname) + ".mol2",
    )

    convert_mol2_to_sybyl_antechamber(
        input_mol2=os.path.join(destination, host_resname) + ".mol2",
        output_mol2=os.path.join(destination, host_resname) + "-sybyl.mol2",
        ac_doctor=False,
    )

    convert_mol2_to_sybyl_antechamber(
        input_mol2=os.path.join(destination, guest_resname) + ".mol2",
        output_mol2=os.path.join(destination, guest_resname) + "-sybyl.mol2",
        ac_doctor=False,
    )

    extract_water_and_ions(
        amber_prmtop=os.path.join(source, reference_prmtop),
        amber_inpcrd=os.path.join(source, reference_inpcrd),
        host_residue=":" + host_resname.upper(),
        guest_residue=":" + guest_resname.upper(),
        dummy_atoms=True,
        output_pdb="water_ions.pdb",
        path=destination,
    )

    if not dummy:
        create_water_and_ions_parameters(
            input_pdb="water_ions.pdb",
            output_prmtop="water_ions.prmtop",
            output_inpcrd="water_ions.inpcrd",
            dummy_atoms=False,
            path=destination,
        )
    else:
        create_water_and_ions_parameters(
            input_pdb="water_ions.pdb",
            output_prmtop="water_ions.prmtop",
            output_inpcrd="water_ions.inpcrd",
            dummy_atoms=True,
            path=destination,
        )

    host = load_mol2(
        filename=os.path.join(destination, host_resname) + "-sybyl.mol2",
        name=host_resname,
        add_tripos=True,
    )

    guest = load_mol2(
        filename=os.path.join(destination, guest_resname) + "-sybyl.mol2",
        name=guest_resname,
        add_tripos=False,
    )

    check_unique_atom_names(host)
    check_unique_atom_names(guest)
    molecules = [host, guest]

    ff = ForceField("forcefield/smirnoff99Frosst.offxml")
    system = ff.createSystem(
        hg_topology.topology,
        molecules,
        nonbondedCutoff=1.1 * unit.nanometer,
        ewaldErrorTolerance=1e-4,
    )

    hg_structure = pmd.openmm.topsystem.load_topology(
        hg_topology.topology, system, hg_topology.positions
    )

    check_bond_lengths(hg_structure, threshold=4)

    try:
        hg_structure.save(os.path.join(destination, "hg.prmtop"))
    except OSError:
        print("Check if the host-guest parameter file already exists...")

    try:
        hg_structure.save(os.path.join(destination, "hg.inpcrd"))
    except OSError:
        print("Check if the host-guest coordinate file already exists...")

    water_and_ions = pmd.amber.AmberParm(
        os.path.join(destination, "water_ions.prmtop"),
        xyz=os.path.join(destination, "water_ions.inpcrd"),
    )

    merged = mergeStructure(hg_structure, water_and_ions)
    merged.box = reference.box
    try:
        merged.save(os.path.join(destination, "smirnoff.prmtop"))
    except:
        print("Check if solvated parameter file already exists...")
    try:
        merged.save(os.path.join(destination, "smirnoff.inpcrd"))
    except:
        print("Check if solvated coordinate file already exists...")

    if not debug:
        clean_up(
            destination=destination,
            host_resname=host_resname,
            guest_resname=guest_resname,
        )

    return merged


def clean_up(destination, host_resname, guest_resname, verbose=False):
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
    water = glob.glob(os.path.join(destination, "water_ions") + "*")
    inpt = glob.glob(os.path.join(destination) + "*.pdb.in")
    outp = glob.glob(os.path.join(destination) + "*.pdb.out")
    host = glob.glob(os.path.join(destination, host_resname) + "*")
    guest = glob.glob(os.path.join(destination, guest_resname) + "*")
    for file in water + host + guest + inpt + outp:
        try:
            if verbose:
                print(f"Removing {file}...")
            os.remove(file)
        except:
            pass
