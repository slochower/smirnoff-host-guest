#!/usr/bin/env python

"""
Provides helper functions for converting AMBER files from an existing force field to
SMIRNOFF99Frosst.
"""

import subprocess as sp
from openeye.oechem import *
from openforcefield.typing.engines.smirnoff import *
from networkx.algorithms import isomorphism


def load_mol2(filename, name=None, add_tripos=True):
    """
    Converts a `mol2` file to an `OEMol` object.
    Parameters
    ----------
    filename : str
        MOL2 file
    name : str
        Residue name
    add_tripos : bool
        Whether to add Tripos atom names to the file

    Returns
    -------
    openeye.oechem.OEMol

    """
    ifs = oemolistream()
    molecules = []
    if not ifs.open(filename):
        print(f'Unable to open {filename} for reading...')
    for mol in ifs.GetOEMols():
        if add_tripos:
            OETriposAtomNames(mol)
        if name:
            mol.SetTitle(name)
        # Add all the molecules in this file to a list, but only return the first one.
        molecules.append(OEMol(mol))
    return molecules[0]


def check_unique_atom_names(molecule):
    """
    Checks to make sure all the atoms in a structure have unique names. This is important for
    host molecules that are composed of multiple residues and thus, may have repeated atom names.
    Parameters
    ----------
    molecule : openeye.oechem.OEMol
    """
    atoms = molecule.GetMaxAtomIdx()
    atom_names = set()
    for atom in range(atoms):
        atom_names.add(molecule.GetAtom(OEHasAtomIdx(atom)).GetName())
    print(f'{atoms} atoms in structure, {len(atom_names)} unique atom names.')
    assert atoms == len(atom_names)

def create_pdb_with_conect(solvated_pdb, amber_prmtop, output_pdb, path='./'):
    """
    Create a PDB file containing CONECT records.
    `cpptraj` must be in your PATH.
    Parameters
    ----------
    solvated_pdb : str
        Existing solvated structure from e.g., Mobley's Benchmark Sets repository
    amber_prmtop : str
        AMBER (or other) parameters for the residues in the solvated PDB file
    output_pdb : str
        Output PDB file name
    path : str
        Directory for input and output files
    """
    cpptraj = \
        f'''
    parm {amber_prmtop}
    trajin {solvated_pdb}
    trajout {output_pdb} conect
    '''

    cpptraj_input = output_pdb + '.in'
    cpptraj_output = output_pdb + '.out'

    with open(path + cpptraj_input, 'w') as file:
        file.write(cpptraj)
    with open(path + cpptraj_output, 'w') as file:
        p = sp.Popen(['cpptraj', '-i', cpptraj_input], cwd=path,
                     stdout=file, stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('PDB file written by cpptraj.')
    elif p.returncode == 1:
        print('Error returned by cpptraj.')
        print(f'Output: {output}')
        print(f'Error: {error}')
        p = sp.Popen(['cat', cpptraj_output], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')


def prune_conect(input_pdb, output_pdb, path='./'):
    """
    Deletes CONECT records that correspond only to water molecules.
    This is necessary to be standards-compliant.
    Parameters
    ----------
    input_pdb : str
        Input PDB file name
    output_pdb : str
        Output PDB file name
    path : str
        Directory for input and output files
    """
    p = sp.Popen(['grep', '-m 1', 'WAT', input_pdb], cwd=path, stdout=sp.PIPE)
    for line in p.stdout:
        first_water_residue = int(float(line.decode("utf-8").split()[1]))
        print(f'First water residue = {first_water_residue}')

    p = sp.Popen(['egrep', '-n', f'CONECT [ ]* {first_water_residue}', input_pdb],
                 cwd=path, stdout=sp.PIPE)
    for line in p.stdout:
        line_to_delete_from = int(float(line.decode("utf-8").split(':')[0]))
        print(f'Found first water CONECT entry at line = {line_to_delete_from}')

    with open(path + output_pdb, 'w') as file:
        sp.Popen(
            ['awk', f'NR < {line_to_delete_from}', input_pdb], cwd=path, stdout=file)

        sp.Popen(['echo', 'END'], cwd=path, stdout=file)


def extract_water_and_ions(amber_prmtop, amber_inpcrd, host_residue, guest_residue,
                           output_pdb, path='./'):
    """
    Create a PDB file containing just the water and ions.
    `cpptraj` must be in your PATH.
    Parameters
    ----------
    amber_prmtop : str
        Existing solvated structure parameters from e.g., Mobley's Benchmark Sets repository
    amber_inpcrd : str
        Existing solvated structure coordinates
    host_residue : str
        Residue name of the host molecule (to be stripped)
    guest_residue : str
        Residue name of the guest molecule (to be stripped)
    output_pdb : str
        Output PDB file name
    path : str
        Directory for input and output files
    """

    cpptraj = \
        f'''
    parm {amber_prmtop}
    trajin {amber_inpcrd}
    strip {host_residue}
    strip {guest_residue}
    trajout {output_pdb}
        '''
    cpptraj_input = output_pdb + '.in'
    cpptraj_output = output_pdb + '.out'

    with open(path + cpptraj_input, 'w') as file:
        file.write(cpptraj)
    with open(path + cpptraj_output, 'w') as file:
        p = sp.Popen(['cpptraj', '-i', cpptraj_input], cwd=path,
                     stdout=file, stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('Water and ion PDB file written by cpptraj.')
    elif p.returncode == 1:
        print('Error returned by cpptraj.')
        print(f'Output: {output}')
        print(f'Error: {error}')
        p = sp.Popen(['cat', cpptraj_output], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')


def create_water_and_ions_parameters(input_pdb, output_prmtop, output_inpcrd,
                                     water_model='tip3p', ion_model='ionsjc_tip3p',
                                     dummy_atoms=False, path='./'):
    """
    Create AMBER coordinates and parameters for just the water and ions.
    `tleap` must be in your PATH.
    Parameters
    ----------
    input_pdb : str
        PDB structure containing everything except the host and guest
    output_prmtop : str
        AMBER parameters for the water and ions
    output_inpcrd : str
        AMBER coordinates for the water and ions
    water_model : str
        Water model, must match AMBER `leaprc.water` and `frcmod`files
    ion_model : str
        Ion model, must match AMBER `leaprc.water` and `frcmod`files
    path : str
        Directory for input and output files
    """

    if dummy_atoms:
        tleap = \
            f'''
        source leaprc.protein.ff14sb
        source leaprc.water.{water_model}
        source leaprc.gaff
        loadamberparams frcmod.{water_model}
        loadamberparams frcmod.{ion_model}
        loadamberparams dum.frcmod
        mol = loadpdb {input_pdb}
        saveamberparm mol {output_prmtop} {output_inpcrd}
        quit
            '''

    else:
        tleap = \
            f'''
        source leaprc.protein.ff14sb
        source leaprc.water.{water_model}
        source leaprc.gaff
        loadamberparams frcmod.{water_model}
        loadamberparams frcmod.{ion_model}
        mol = loadpdb {input_pdb}
        saveamberparm mol {output_prmtop} {output_inpcrd}
        quit
            '''
    tleap_input = output_prmtop + '.in'
    tleap_output = output_prmtop + '.out'

    with open(path + tleap_input, 'w') as file:
        file.write(tleap)
    with open(path + tleap_output, 'w') as file:
        p = sp.Popen(['tleap', '-f', tleap_input, '>', tleap_output], cwd=path,
                     stdout=file, stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('Water and ion parameters and coordinates written by tleap.')
    elif p.returncode == 1:
        print('Error returned by tleap.')
        print(f'Output: {output}')
        print(f'Error: {error}')
        p = sp.Popen(['cat', tleap_output], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
        p = sp.Popen(['cat', 'leap.log'], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')

def process_smiles(string, name=None, add_hydrogens=True, add_tripos=True):
    mol = OEMol()
    OESmilesToMol(mol, string)
    if add_hydrogens:
        OEAddExplicitHydrogens(mol)
    if add_tripos:
        OETriposAtomNames(mol)
    if name:
        mol.SetTitle(name)
    return mol


def atom_mapping(reference, target):
    reference_topology = create_topology(reference)
    target_topology = create_topology(target)

    reference_graph = create_graph(reference_topology)
    target_graph = create_graph(target_topology)

    reference_to_target_mapping = dict()
    graph_matcher = isomorphism.GraphMatcher(reference_graph, target_graph)
    if graph_matcher.is_isomorphic():
        print('Determining mapping...')
        print('Reference → Target')
        for (reference_atom, target_atom) in graph_matcher.mapping.items():
            reference_to_target_mapping[reference_atom] = target_atom
            reference_name = reference.GetAtom(OEHasAtomIdx(reference_atom)).GetName()
            reference_type = reference.GetAtom(OEHasAtomIdx(reference_atom)).GetType()
            target_name = target.GetAtom(OEHasAtomIdx(target_atom)).GetName()

            print(f'({reference_name:4} {reference_type:5}) {reference_atom:3d} → '
                  f'{target_atom:3d} ({target_name:4})')
    else:
        print('Graph is not isomorphic.')
    return reference_to_target_mapping


def create_topology(mol):
    return generateTopologyFromOEMol(mol)


def create_graph(topology):
    return generateGraphFromTopology(topology)


def remap_charges(reference_to_target_mapping, reference_mol, target_mol):
    print('Remapping charges...')
    print('Existing → New')
    assert reference_mol.GetMaxAtomIdx() == target_mol.GetMaxAtomIdx()
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        reference = reference_mol.GetAtom(OEHasAtomIdx(reference_atom))
        reference_chg = reference.GetPartialCharge()

        target = target_mol.GetAtom(OEHasAtomIdx(target_atom))
        # This will be zero, if the target molecule was built from SMILES
        target_chg = target.GetPartialCharge()
        target_name = target.GetName()

        target.SetPartialCharge(reference_chg)
        print(f'({target_name:4}) {target_chg:+04f} → {target.GetPartialCharge():+04f}')
    return target_mol


def remap_names(reference_to_target_mapping, reference_mol, target_mol):
    print('Remapping atom names...')
    print('Reference → Target')
    assert reference_mol.GetMaxAtomIdx() == target_mol.GetMaxAtomIdx()
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        reference = reference_mol.GetAtom(OEHasAtomIdx(reference_atom))
        reference_name = reference.GetName()

        target = target_mol.GetAtom(OEHasAtomIdx(target_atom))
        target_name = target.GetName()
        target.SetName(reference_name)
        print(f'{reference_name:4} → {target_name:4}')
    return target_mol


def parse_residue_name(input_mol2, path='./'):
    p = sp.Popen(['awk', '{print $8}', input_mol2], cwd=path, stdout=sp.PIPE)
    for line in p.stdout:
        if line.decode("utf-8").split() != []:
            name = line.decode("utf-8").split()[0]
            print(f'Found residue name = {name}')
            return name
        else:
            pass
    return None


def remap_residues(reference_to_target_mapping, reference_mol, target_mol, resname=None):
    print('Remapping residue names and numbers...')
    print('Existing → New')
    assert reference_mol.GetMaxAtomIdx() == target_mol.GetMaxAtomIdx()
    # It's not clear to me that we have to loop over all the atoms in the molecule,
    # if OpenEye knows they are connected properly, then setting the residue name
    # and residue number for one atom should be enough, but keeping this loop
    # seems safe and won't be a bottleneck.
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        reference = reference_mol.GetAtom(OEHasAtomIdx(reference_atom))
        reference_residue = OEAtomGetResidue(reference)
        reference_resname = reference_residue.GetName()
        reference_resnum = reference_residue.GetResidueNumber()
        # I believe this gets set to 'UNL' if OpenEye can't recognize the residue name.
        # Thus, I'm adding an override to manually set the residue name, and simply.

        target = target_mol.GetAtom(OEHasAtomIdx(target_atom))
        target_name = target.GetName()
        target_residue = OEAtomGetResidue(target)
        target_resname = target_residue.GetName()
        target_resnum = target_residue.GetResidueNumber()

        if resname is not None:
            target_residue.SetName(resname)
        else:
            target_residue.SetName(reference_resname)
        target_residue.SetResidueNumber(reference_resnum)

        print(f'({target_name:4}) {target_resname:4} {target_resnum:4} → '
              f'{target_residue.GetName():4} {target_residue.GetResidueNumber():4}')
    return target_mol


def remap_type(reference_to_target_mapping, reference_mol, target_mol):
    print('Remapping atom types...')
    print('Existing → New')
    assert reference_mol.GetMaxAtomIdx() == target_mol.GetMaxAtomIdx()
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        reference = reference_mol.GetAtom(OEHasAtomIdx(reference_atom))
        reference_type = reference.GetType()

        target = target_mol.GetAtom(OEHasAtomIdx(target_atom))
        # This will be None, if the target molecule was built from SMILES
        target_type = target.GetType()
        target_name = target.GetName()

        target.SetType(reference_type)
        print(f'({target_name:4}) {target_type:4} → {target.GetType():4}')
    return target_mol


def remap_coordinates(reference_to_target_mapping, reference_mol, target_mol):
    print('Remapping coordinates...')
    print('Existing → New')
    assert reference_mol.GetMaxAtomIdx() == target_mol.GetMaxAtomIdx()
    mapped_coordinates = np.zeros((reference_mol.GetMaxAtomIdx(), 3))
    reference_coordinates = reference_mol.GetCoords()
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        mapped_coordinates[target_atom] = reference_coordinates[reference_atom]
        current_coordinates = target_mol.GetCoords()[target_atom]
        print(f'{current_coordinates} → {mapped_coordinates[target_atom]}')
    target_mol.SetCoords(mapped_coordinates.flatten())
    return target_mol
