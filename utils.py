def create_pdb_with_conect(solvated_pdb, amber_prmtop, output_pdb, path='./'):
    """
    Create a PDB file containing CONECT records.
    This is not very robust, please manually check the `cpptraj` output.
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
    Delete CONECT records that correspond only to water molecules.
    This is necessary to be standards-compliant.
    This is not very robust.
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


def load_mol2(filename, name=None, add_tripos=True):
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
    atoms = molecule.GetMaxAtomIdx()
    atom_names = set()
    for atom in range(atoms):
        atom_names.add(molecule.GetAtom(OEHasAtomIdx(atom)).GetName())
    print(f'{atoms} atoms in structure, {len(atom_names)} unique atom names.')
    assert atoms == len(atom_names)


def extract_water_and_ions(amber_prmtop, amber_inpcrd, host_residue, guest_residue,
                           output_pdb, path='./'):
    """
    Create a PDB file containing just the water and ions.
    This is not very robust, please manually check the `cpptraj` output.
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
                                     path='./'):
    """
    Create AMBER coordinates and parameters for just the water and ions.
    This is not very robust, please manually check the `tleap` output.
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
    else:
        print(f'Output: {output}')
        print(f'Error: {error}')
