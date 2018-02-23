#!/usr/bin/env python
"""
Provides helper functions for converting AMBER files from an existing force field to
SMIRNOFF99Frosst.
"""

import subprocess as sp
import parmed as pmd
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


def save_mol2(molecule, filename):
    """
    Saves an `OEMol` object as `mol2` file.
    Parameters
    ----------
    molecule : openeye.oechem.OEMol
        Molecule to save
    filename : str
        MOL2 file

    """
    ofs = oemolostream()
    ofs.SetFormat(OEFormat_MOL2H)
    if ofs.open(filename):
        OEWriteMolecule(ofs, molecule)
    else:
        pint(f'Unable to open {filename} for writing...')


def convert_mol2_to_sybyl(input_mol2, output_mol2):
    """
    Convert an otherwise formatted `mol2` file into a `mol2` file with SYBYL atom types.
    
    Parameters:
    ----------
    input_mol2 : str
        File name of existing `mol2`
    output_mol2 : str
        File name of destination `mol2`
    """
    structure = load_mol2(input_mol2)
    save_mol2(structure, output_mol2)


def load_pdb(filename, name=None, add_tripos=True):
    """
    Converts a `pdb` file to an `OEMol` object. By default, this will read dummy atoms.
    Parameters
    ----------
    filename : str
        PDB file
    name : str
        Residue name
    add_tripos : bool
        Whether to add Tripos atom names to the file

    Returns
    -------
    openeye.oechem.OEMol

    """
    ifs = oemolistream()
    flavor = oechem.OEIFlavor_Generic_Default | oechem.OEIFlavor_PDB_Default | oechem.OEIFlavor_PDB_ALL
    ifs.SetFlavor(OEFormat_PDB, flavor)

    molecules = []
    if not ifs.open(filename):
        print(f'Unable to open {filename} for reading...')
    for mol in ifs.GetOEGraphMols():
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
        p = sp.Popen(
            ['cpptraj', '-i', cpptraj_input],
            cwd=path,
            stdout=file,
            stderr=file)
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

    p = sp.Popen(
        ['egrep', '-n', f'CONECT [ ]* {first_water_residue}', input_pdb],
        cwd=path,
        stdout=sp.PIPE)
    for line in p.stdout:
        line_to_delete_from = int(float(line.decode("utf-8").split(':')[0]))
        print(
            f'Found first water CONECT entry at line = {line_to_delete_from}')

    with open(path + output_pdb, 'w') as file:
        sp.Popen(
            ['awk', f'NR < {line_to_delete_from}', input_pdb],
            cwd=path,
            stdout=file)

        sp.Popen(['echo', 'END'], cwd=path, stdout=file)


def extract_dummy_atoms(amber_prmtop,
                        amber_inpcrd,
                        dummy_residue,
                        output_pdb,
                        path='./'):
    cpptraj = \
        f'''
    parm {amber_prmtop}
    trajin {amber_inpcrd}
    strip !{dummy_residue}
    trajout {output_pdb}
        '''

    cpptraj_input = output_pdb + '.in'
    cpptraj_output = output_pdb + '.out'

    with open(path + cpptraj_input, 'w') as file:
        file.write(cpptraj)
    with open(path + cpptraj_output, 'w') as file:
        p = sp.Popen(
            ['cpptraj', '-i', cpptraj_input],
            cwd=path,
            stdout=file,
            stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('Dummy atom PDB file written by cpptraj.')
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


def extract_water_and_ions(amber_prmtop,
                           amber_inpcrd,
                           host_residue,
                           guest_residue,
                           output_pdb,
                           dummy=None,
                           path='./'):
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

    if dummy is None:
        cpptraj = \
            f'''
parm {amber_prmtop}
trajin {amber_inpcrd}
strip {host_residue}
strip {guest_residue}
trajout {output_pdb}
            '''

    else:
        cpptraj = \
            f'''
parm {amber_prmtop}
trajin {amber_inpcrd}
strip {host_residue}
strip {guest_residue}
strip {dummy}
trajout {output_pdb}
            '''

    cpptraj_input = output_pdb + '.in'
    cpptraj_output = output_pdb + '.out'

    with open(path + cpptraj_input, 'w') as file:
        file.write(cpptraj)
    with open(path + cpptraj_output, 'w') as file:
        p = sp.Popen(
            ['cpptraj', '-i', cpptraj_input],
            cwd=path,
            stdout=file,
            stderr=file)
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


def create_dummy_atom_parameters(input_pdb,
                                 output_prmtop,
                                 output_inpcrd,
                                 path='./'):
    write_dummy_atom_frcmod(file_name='frcmod.dum', path=path)
    write_dummy_atom_mol2(file_name='dum.mol2', path=path)
    tleap = \
        f'''
    source leaprc.protein.ff14sb
    source leaprc.gaff
    loadamberparams frcmod.dum
    DUM = loadmol2 dum.mol2
    mol = loadpdb {input_pdb}
    saveamberparm mol {output_prmtop} {output_inpcrd}
    quit
        '''

    tleap_input = output_prmtop + '.in'
    tleap_output = output_prmtop + '.out'

    with open(path + tleap_input, 'w') as file:
        file.write(tleap)
    with open(path + tleap_output, 'w') as file:
        p = sp.Popen(
            ['tleap', '-f', tleap_input, '>', tleap_output],
            cwd=path,
            stdout=file,
            stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('Dummy atom  parameters and coordinates written by tleap.')
    elif p.returncode == 1:
        print('Error returned by tleap.')
        print(f'Output: {output}')
        print(f'Error: {error}')
        p = sp.Popen(['cat', tleap_output], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
        # Because `leap.log` is hardcoded, only some output ends up in the desired output file.
        p = sp.Popen(['cat', 'leap.log'], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')


def create_water_and_ions_parameters(input_pdb,
                                     output_prmtop,
                                     output_inpcrd,
                                     water_model='tip3p',
                                     ion_model='ionsjc_tip3p',
                                     dummy_atoms=False,
                                     path='./'):
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
        write_dummy_atom_frcmod(file_name='frcmod.dum', path=path)
        write_dummy_atom_mol2(file_name='dum.mol2', path=path)
        tleap = \
            f'''
        source leaprc.protein.ff14sb
        source leaprc.water.{water_model}
        source leaprc.gaff
        loadamberparams frcmod.{water_model}
        loadamberparams frcmod.{ion_model}
        loadamberparams frcmod.dum
        DUM = loadmol2 dum.mol2
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
        p = sp.Popen(
            ['tleap', '-f', tleap_input, '>', tleap_output],
            cwd=path,
            stdout=file,
            stderr=file)
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
        # Because `leap.log` is hardcoded, only some output ends up in the desired output file.
        p = sp.Popen(['cat', 'leap.log'], cwd=path, stdout=sp.PIPE)
        for line in p.stdout:
            print(line.decode("utf-8").strip(), )
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')


def write_dummy_atom_frcmod(file_name, path='./'):
    """
    Create a `frcmod` file to handle dummy atoms in structures.
    
    Parameters:
    ----------
    file_name : str
        Name of `frcmod` file to be written
    path : str
        Directory of `frcmod` file to be written
    """

    frcmod = \
        '''Parameters for a "Lead-like" Dummy Atom
MASS
Pb     210.00

BOND

ANGLE

DIHE

IMPROPER

NONBON
Pb       0.000     0.0000000

        '''
    with open(path + file_name, 'w') as file:
        file.write(frcmod)
    print('Writing dummy atom `frcmod`.')


def write_dummy_atom_mol2(file_name, path='./'):
    """
    Create a `mol2` file to handle dummy atoms in structures.
    
    Parameters:
    ----------
    file_name : str
        Name of `mol2` file to be written
    path : str
        Directory of `mol2` file to be written
    """

    mol2 = \
        '''@<TRIPOS>MOLECULE
DUM
    1     0     1     0     1
SMALL
USER_CHARGES
@<TRIPOS>ATOM
  1 Pb      0.000000    0.000000    0.000000 Pb    1 DUM     0.0000 ****
@<TRIPOS>BOND
@<TRIPOS>SUBSTRUCTURE
      1  DUM              1 ****               0 ****  ****
        '''
    with open(path + file_name, 'w') as file:
        file.write(mol2)
    print('Writing dummy atom `mol2`.')


def process_smiles(string, name=None, add_hydrogens=True, add_tripos=True):
    """Wrapper for a few options to convert a SMILES string to an OEMol.
    
    Parameters:
    ----------
    string : str
        SMILES string
    name :str, optional
       Residue name of the molecule
    add_hydrogens : bool
        Whether to add explicit hydrogens or not
    add_tripos : bool
        Whether to assign Tripos atom names, and thus make all atoms names unique
    
    Returns
    -------
    openeye.oechem.OEMol
        The molecule
    """

    mol = OEMol()
    OESmilesToMol(mol, string)
    if add_hydrogens:
        OEAddExplicitHydrogens(mol)
    if add_tripos:
        OETriposAtomNames(mol)
    if name:
        mol.SetTitle(name)
    return mol


def map_atoms(reference_mol, target_mol):
    """
    Maps between a reference molecule and target molecule using maximum common substructure. For more information, see the example here: https://github.com/openforcefield/openforcefield/blob/6229a51ad77fd5cf20299e53bc9784811cb9443a/openforcefield/typing/engines/smirnoff/forcefield.py#L350
    
    Parameters:
    ----------
    reference_mol : openeye.oechem.OEMol
        Reference molecule for mapping
    target_mol : openeye.oechem.OEMol
        Target molecule for mapping
    Returns
    -------
    dictionary
        The mapping between atom numbers in each molecule
    """

    reference_topology = create_topology(reference_mol)
    target_topology = create_topology(target_mol)

    reference_graph = create_graph(reference_topology)
    target_graph = create_graph(target_topology)

    reference_to_target_mapping = dict()
    graph_matcher = isomorphism.GraphMatcher(reference_graph, target_graph)
    if graph_matcher.is_isomorphic():
        print('Determining mapping...')
        print('Reference → Target')
        for (reference_atom, target_atom) in graph_matcher.mapping.items():
            reference_to_target_mapping[reference_atom] = target_atom
            reference_name = reference_mol.GetAtom(
                OEHasAtomIdx(reference_atom)).GetName()
            reference_type = reference_mol.GetAtom(
                OEHasAtomIdx(reference_atom)).GetType()
            target_name = target_mol.GetAtom(
                OEHasAtomIdx(target_atom)).GetName()
            print(f'({reference_name:5} {reference_atom:3d} → '
                  f'{target_atom:3d} ({target_name:5})')
    else:
        print('Graph is not isomorphic.')

    return reference_to_target_mapping


def map_residues(reference_to_target_mapping, reference_mol, target_mol):
    """
    Maps between a reference molecule and target molecule using an existing atom mapping. For more information, see the example here: https://github.com/openforcefield/openforcefield/blob/6229a51ad77fd5cf20299e53bc9784811cb9443a/openforcefield/typing/engines/smirnoff/forcefield.py#L350
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        Atom mapping calculated using `map_atoms()`
    reference_mol : openeye.oechem.OEMol
        Reference molecule for mapping
    target_mol : openeye.oechem.OEMol
        Target molecule for mapping
    Returns
    -------
    dictionary
        The mapping between residue numbers in each molecule
    """

    reference_to_target_residue_mapping = dict()
    print('Reference → Target')
    for (reference_atom, target_atom) in reference_to_target_mapping.items():
        reference = reference_mol.GetAtom(OEHasAtomIdx(reference_atom))
        reference_name = reference.GetName()
        reference_residue = OEAtomGetResidue(reference)
        reference_resname = reference_residue.GetName()
        reference_resnum = reference_residue.GetResidueNumber()

        target = target_mol.GetAtom(OEHasAtomIdx(target_atom))
        target_name = target.GetName()
        target_residue = OEAtomGetResidue(target)
        target_resname = target_residue.GetName()
        target_resnum = target_residue.GetResidueNumber()
        reference_to_target_residue_mapping[reference_resnum] = target_resnum

        print(
            f'{reference_name:5} {reference_resname:5} ({reference_atom:4d}) {reference_resnum:4d} → {target_resnum:4d} ({target_atom:4d}) {target_name:5} {target_resname:5}'
        )

    return reference_to_target_residue_mapping


def create_topology(mol):
    return generateTopologyFromOEMol(mol)


def create_graph(topology):
    return generateGraphFromTopology(topology)


def remap_charges(reference_to_target_mapping, reference_mol, target_mol):
    """Copies charges from a reference molecule to a target molecule.
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    reference_mol : openeye.oechem.OEMol
        Reference molecule
    target_mol : openeye.oechem.OEMol
        Target molecule
    Returns
    -------
    openey.oechem.OEMol
        The target molecule with charges from the reference molecule
    """

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
        print(
            f'({target_name:4}) {target_chg:+04f} → {target.GetPartialCharge():+04f}'
        )
    return target_mol


def remap_names(reference_to_target_mapping, reference_mol, target_mol):
    """Copies atom names from the reference molecule to the target molecule.
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    reference_mol : openeye.oechem.OEMol
        Reference molecule
    target_mol : openeye.oechem.OEMol
        Target molecule
    Returns
    -------
    openey.oechem.OEMol
        The target molecule with atom names from the reference molecule
    """

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


def remap_type(reference_to_target_mapping, reference_mol, target_mol):
    """Copies atom types from the reference molecule to the target molecule.
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    reference_mol : openeye.oechem.OEMol
        Reference molecule
    target_mol : openeye.oechem.OEMol
        Target molecule
    Returns
    -------
    openey.oechem.OEMol
        The target molecule with atom types from the reference molecule
    """
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
    """Copies atom coordinates from the reference molecule to the target molecule.
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    reference_mol : openeye.oechem.OEMol
        Reference molecule
    target_mol : openeye.oechem.OEMol
        Target molecule
    Returns
    -------
    openey.oechem.OEMol
        The target molecule with atom coordinates from the reference molecule
    """
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


def remap_residues(reference_to_target_mapping,
                   reference_mol,
                   target_mol,
                   resname=None):
    """Copies residue name and number from the reference molecule to the target molecule.
    
    Parameters:
    ----------
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    reference_mol : openeye.oechem.OEMol
        Reference molecule
    target_mol : openeye.oechem.OEMol
        Target molecule
    resname : str
        Override setting the target residue name
    Returns
    -------
    openey.oechem.OEMol
        The target molecule with residue name and number from the reference molecule
    """
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
        # Thus, I'm adding an override to manually set the residue name.

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

        print(
            f'({target_name:4}) {target_resname:4} {target_resnum:4} → '
            f'{target_residue.GetName():4} {target_residue.GetResidueNumber():4}'
        )
    return target_mol


def parse_residue_name(input_mol2, path='./'):
    """Extract the residue name from a `mol2` file.
    
    Parameters:
    ----------
    input_mol2 : str
        File name of the `mol2`
    Returns
    -------
    str or None
        Residue name, if found
    """

    p = sp.Popen(['awk', '{print $8}', input_mol2], cwd=path, stdout=sp.PIPE)
    for line in p.stdout:
        if line.decode("utf-8").split() != []:
            name = line.decode("utf-8").split()[0]
            print(f'Found residue name = {name}')
            return name
        else:
            pass
    return None


def split_topology(file_name):
    """Split a file into component topology using ParmEd.
    
    Parameters:
    ----------
    file_name : str
        Structure file
    """

    topology = pmd.load_file(file_name)
    return topology.split()


def create_host_guest_topology(components, host_resname, guest_resname):
    """Return the topology components belonging the host and guest only.
    
    Parameters:
    ----------
    components : parmed.topology.components
        ParmEd topology components, split by molecule
    host_resname : str
        Residue name of the host molecule (no colon)
    guest_resname : str
        Residue name of the guest molecule (no colon)
    Returns
    -------
    pmd.Structure
        A ParmEd structure containing just the host and guest molecule
    """
    topology = pmd.Structure()
    for component in components:
        # Check the first residue of each component becuase there may be multiple residues in each component, but they shoudl all have the same residue name.hash
        if component[0].residues[0].name == host_resname.upper() or \
            component[0].residues[0].name == guest_resname.upper():
            topology += component[0]
    return topology


def create_host_mol2(solvated_pdb, amber_prmtop, mask, output_mol2, path='./'):
    """
    Create a `mol2` file for the host (useful if the host is composed of multiple residues).
    `cpptraj` must be in your PATH.
    Parameters
    ----------
    solvated_pdb : str
        Existing solvated structure from e.g., Mobley's Benchmark Sets repository
    amber_prmtop : str
        AMBER (or other) parameters for the residues in the solvated PDB file
    mask : str
        AMBER mask to select the host (without colon)
    output_mol2 : str
        Output `mol2` file name
    path : str
        Directory for input and output files
    """
    cpptraj = \
        f'''
    parm {amber_prmtop}
    trajin {solvated_pdb}
    mask ":{mask}" maskmol2 {output_mol2}
    '''

    cpptraj_input = output_mol2 + '.in'
    cpptraj_output = output_mol2 + '.out'

    with open(path + cpptraj_input, 'w') as file:
        file.write(cpptraj)
    with open(path + cpptraj_output, 'w') as file:
        p = sp.Popen(
            ['cpptraj', '-i', cpptraj_input],
            cwd=path,
            stdout=file,
            stderr=file)
        output, error = p.communicate()
    if p.returncode == 0:
        print('MOL2 file written by cpptraj.')
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
    # Since `cpptraj` writes the frame number as suffix, move back to desired file name.
    p = sp.Popen(
        ['mv', output_mol2 + '.1', output_mol2], cwd=path, stdout=sp.PIPE)


def copy_box_vectors(input_inpcrd, output_inpcrd, path='./'):
    """    
    Copy the last line of an existing AMBER `inpcrd` file containing the box vectors and angles to a new `inpcrd`. This helps when the box vector information has been lost. This runs with `shell=True`, so it could be dangerous; I was unable to get this to work with `sp.Popen()`.

    Parameters:
    ----------
    input_inpcrd : str
        File name of reference `inpcrd`
    output_inpcrd : str
        File name of target `inpcrd`
    """

    p = sp.call(
        [f'tail -n 1 {input_inpcrd} >> {output_inpcrd}'], cwd=path, shell=True)


def rewrite_restraints_file(reference_restraints,
                            target_restraints,
                            reference_to_target_mapping,
                            path='./'):
    """
    Rewrite an existing AMBER restraint file using the *atom* mapping between the two structures. Only the field `iat= ` is modified. 
    
    Caveat: this function assumes a fixed-width format of the restraint file (i.e., 18 characters between `iat= ` and `r1= ` -- which works well for us, here -- although I do not believe that is a firm requirement on the AMBER side of things.

    Parameters:
    ----------
    reference_restraints : str
        File name of reference restraints file
    target_restraits : str
        File name of target restraints file
    reference_to_target_mapping : dict
        The dictionary containing the mapping between atoms in the reference and target molecules
    """

    # First, read the existing file...
    with open(reference_restraints, 'r') as disang:
        lines = []
        for line in disang:
            lines.append(line)

    # Next, rewrite using the fact that Niel has a fixed width for the atom index section...
    with open(target_restraints, 'w') as my_disang:
        my_disang.write(lines[0])
        for line in lines[1:]:
            old_restraint_list = line.split()[2]
            old_restraint_residues = [
                int(i) for i in old_restraint_list.split(',') if i is not ''
            ]

            new_restraint_residues = []
            for atom_index in old_restraint_residues:
                new_restraint_residues.append(
                    reference_to_target_mapping[atom_index - 1] + 1)
            # Join the residues with commas
            new_restraint_string = ','.join(
                [str(i) for i in new_restraint_residues])
            print(f'{old_restraint_list:18} → {new_restraint_string:18}')
            new_line = line[0:10] + '{0: <18}'.format(
                new_restraint_string) + line[27:]
            my_disang.write(new_line)


def rewrite_amber_input_file(reference_input,
                             target_input,
                             reference_to_target_mapping,
                             path='./'):
    """
    Rewrite an existing AMBER simulation input file using the *residue* mapping between the two structures. Only the positional restraints, specified by `restraintmask` are rewritten.
    
    Parameters:
    ----------
    reference_input : str
        File name of reference restraints file
    target_input : str
        File name of target restraints file
    reference_to_target_mapping : dict
        The dictionary containing the mapping between residues in the reference and target molecules
    """

    # First, read the existing file...
    with open(reference_input, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)

    with open(target_input, 'w') as file:
        for line_number, line in enumerate(lines):
            # This should gracefully just copy the reference to the target if there are no positional restraints...
            if 'restraintmask' in line:
                restraint_mask = line.split()[2:]
                restraint_mask_line = line_number
            else:
                pass

        new_masks = []
        for mask in restraint_mask:
            # Detect the residue mask by the colon...
            if ':' in mask:
                # Get rid of the preceeding apostrophe...
                if "'" in mask:
                    mask = mask.replace("'", "")
                # Get rid of the comma...
                if "," in mask:
                    mask = mask.replace(",", "")
                # Now, I expect that we should have one or more masks joined by '|'
                # Split each mask into one ore more residues...
                if '-' in mask[1:]:
                    # If the mask is a range, parse each residue separately...
                    residues = split('-', mask[1:])
                    new_residues = []
                    for residue in residues:
                        new_residue = reference_to_target_mapping[int(residue)]
                        new_residues.append(str(new_residue))
                else:
                    # If the mask is atom-based, we only want to modify the residue portion...
                    residues = split('@', mask[1:])
                    new_residues = []
                    for residue in residues[:1]:
                        new_residue = reference_to_target_mapping[int(residue)]
                        new_residues.append(str(new_residue))
                if len(new_residues) > 1:
                    new_mask = ':' + '-'.join(new_residues)
                else:
                    new_mask = ':' + new_residues[0] + '@' + residues[1:][0]
                new_masks.append(new_mask)

        new_restraint_mask = '\'' + ' | '.join(new_masks) + '\'' + ','
        print(f'{restraint_mask} → {new_restraint_mask}')
        # Rewrite this single line in `lines` array containing the contents of the reference file...
        lines[
            restraint_mask_line] = '  restraintmask = ' + new_restraint_mask + '\n'
        for line in lines:
            file.write(line)


def split(delimiters, string, maxsplit=0):
    # https://stackoverflow.com/a/13184791
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)


def color_restraints(restraint_file, color, suffix, md_file, path='./'):
    """
    Write a bash script to render restraints in Chimera using the atom indices specifed in an AMBER restraint file (i.e., `disang.rest`).

    Parameters:
    ----------
    restraint_file : str
        AMBER restraint file
    color : str
        Color of restraints in Chimera
    suffix : str
        Suffix of Chimera command and rendered files
    md_file : str
        Chimera "metafile" to load trajectory 
        # http://plato.cgl.ucsf.edu/pipermail/chimera-users/2015-May/011036.html
    """

    try:
        os.stat(path)
    except:
        os.mkdir(path)

    # First, read the existing file...
    with open(restraint_file, 'r') as disang:
        with open(f'{path}/render-{suffix}.sh', 'w') as script:

            lines = []
            for line in disang:
                lines.append(line)

            for line_index, line in enumerate(lines[1:]):
                old_restraint_list = line.split()[2]
                old_restraint_residues = [
                    int(i) for i in old_restraint_list.split(',')
                    if i is not ''
                ]

                with open(f'{path}/restraint-{line_index:02.0f}-{suffix}.cmd',
                          'w') as chimera:
                    chimera.write('sleep 1\n')
                    chimera.write('~display :WAT\n')
                    chimera.write('~display :Na+\n')
                    chimera.write('turn y 90\n')
                    chimera.write('color grey\n')

                    for residue in old_restraint_residues:
                        chimera.write(
                            f'color {color} @/serialNumber={residue}\n')
                        chimera.write(f'repr bs @/serialNumber={residue}\n')

                    chimera.write(
                        f'2dlabel create title text "{old_restraint_list}" xpos 0.1 ypos 0.92 color black\n'
                    )

                    chimera.write(
                        f'copy file restraint-{line_index:02.0f}-{suffix}.png\n'
                    )
                    chimera.write('stop')
                    script.write(
                        f'chimera md:{md_file} restraint-{line_index:02.0f}-{suffix}.cmd \n'
                    )