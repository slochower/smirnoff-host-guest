#!/usr/bin/env python
"""
Provides a wrapper to change SMIRNOFF99Frosst "atom types" to two-character unique atom types.
"""
import parmed as pmd

CHARS = "0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r\
            s t u v w x y z A B C D E F G H I J K L M N O P Q R S T\
            U V W X Y Z * & $ # % [ ] { } < > ? + = : ; ' . , ! ~ `\
            @ ^ ( ) _ | / \\ \"".split()


def create_element_type_lists(first_chars, second_chars):
    """ Create two character atom types. """
    return [first_char + second_char for first_char in first_chars for second_char in second_chars]


def create_mapping(structure, host_resname, guest_resname):
    """
    Create a mapping between position in a residue (i.e., the "first" atom when iterating through the atoms in a
    residue) and fake atom types that depend on the element. This is useful for at least two reasons: first,
    it can eliminate the need to use three character atom types for a while (we can have 26**3 unique types per
    element here -- that's more than 17,000 types of hydrogen) and second, SMIRNOFF99Frosst parameterizes every atom
    as a unique entity so C1 in the first MGO residue will be typed differently than C1 in the second MGO residue,
    even though the parameters will be the same (as they should be for chemically identical atoms). Having different
    types makes it effectively impossible to run this through `tleap` and other utilities.

    Parameters
    ----------
    structure : pmd.Structure
        A ParmEd structure with SMIRNOFF99Frosst numeric atom types
    host_resname : str
        Residue name of the host molecule
    guest_resname : str
        Residue name of the guest molecule

    Returns
    -------
    host_mapping : dict
        Dictionary mapping between original host atom types and the new types
    guest_mapping : dict
        Dictionary mapping between original guest atom typse and the new types
    """

    hydrogen_list = create_element_type_lists(['H', 'h', '1'], CHARS)
    carbon_list = create_element_type_lists(['C', 'c', '6'], CHARS)
    oxygen_list = create_element_type_lists(['O', 'o', '8'], CHARS)
    nitrogen_list = create_element_type_lists(['N', 'n', '7'], CHARS)

    host_mapping = dict()
    guest_mapping = dict()
    hydrogen_index = 0
    carbon_index = 0
    nitrogen_index = 0
    oxygen_index = 0

    for residue in structure.residues:
        if residue.name == host_resname and not host_mapping:
            for atom_index, atom in enumerate(residue):
                # WARNING
                # Assumption: each host residue has atoms numbered in the same order!
                # This is going to greatly simplify assigning unique atom types *only* within a residue.
                # To be completely thorough, we could add a check here that the parameters associated with each
                # atom type in each residue are identical, but for now I've manually checked this is correct.
                if atom.element == 1:
                    host_mapping[atom_index], hydrogen_index = hydrogen_list[hydrogen_index]
                    hydrogen_index += 1
                elif atom.element == 6:
                    host_mapping[atom_index] = carbon_list[carbon_index]
                    carbon_index += 1
                elif atom.element == 7:
                    host_mapping[atom_index] = nitrogen_list[nitrogen_index]
                    nitrogen_index += 1
                elif atom.element == 8:
                    host_mapping[atom_index] = oxygen_list[oxygen_index]
                    oxygen_index += 1
                else:
                    print(f'Whoops, missing atom type lists for element {atom.element}.')
        elif residue.name == guest_resname and not guest_mapping:
            for atom_index, atom in enumerate(residue):
                if atom.element == 1:
                    guest_mapping[atom_index] = hydrogen_list[hydrogen_index]
                    hydrogen_index += 1
                elif atom.element == 6:
                    guest_mapping[atom_index] = carbon_list[carbon_index]
                    carbon_index += 1
                elif atom.element == 7:
                    guest_mapping[atom_index] = nitrogen_list[nitrogen_index]
                    nitrogen_index += 1
                elif atom.element == 8:
                    guest_mapping[atom_index] = oxygen_list[oxygen_index]
                    oxygen_index += 1
                else:
                    print(f'Whoops, missing atom type lists for this element {atom.element}')
    return host_mapping, guest_mapping


def remap_atom_types(AmberParm, host_resname, host_mapping, guest_resname, guest_mapping, destination):
    """
    Remap atom types given a dictionary.

    Parameters
    ----------
    AmberParm : pmd.amber.AmberParm
        A parameter set from ParmEd (*not* a Structure)
    host_resname : str
        Residue name of the host molecule
    host_mapping : dict
        Mapping between old and new atom types by *position* in the residue
    guest_resname : str
        Residue name of the guest molecule
    guest_mapping : dict
        Mapping between old and new atom types by *position* in the residue
    destination : str
        Path for the output files (which will be overwritten)

    """
    for residue in AmberParm.residues:
        if residue.name == host_resname:
            for index, atom in enumerate(residue):
                print(f'Assigning {residue.number} {atom.name} {atom.type} → {host_mapping[index]}')
                AmberParm.parm_data['AMBER_ATOM_TYPE'][int(atom.type) - 1] = host_mapping[index]
                atom.type = host_mapping[index]
        if residue.name == guest_resname:
            for index, atom in enumerate(residue):
                print(f'Assigning {residue.number} {atom.name} {atom.type} → {guest_mapping[index]}')

                # This is not working correctly!
                AmberParm.parm_data['AMBER_ATOM_TYPE'][int(atom.type) - 1] = guest_mapping[index]
                atom.type = guest_mapping[index]

    AmberParm.load_atom_info()
    AmberParm.fill_LJ()
    AmberParm.save(destination + 'smirnoff-unique.mol2', overwrite=True)
    AmberParm.save(destination + 'smirnoff-unique.prmtop', overwrite=True)

    parameter_set = pmd.amber.AmberParameterSet.from_structure(AmberParm)
    parameter_set.write(destination + 'smirnoff-unique.frcmod')

    # Read back in the `prmtop`...
    structure = pmd.load_file(destination + 'smirnoff-unique.prmtop', structure=True)

    # Write out a `mol2` file for the guest -- expecting all atom types to begin with `G`...
    single_guest = structure[':' + guest_resname]
    single_guest.save(destination + 'smirnoff-' + guest_resname + '-unique.mol2', overwrite=True)

    single_host = structure[
        ':' + str(structure[':' + host_resname].residues[0].number + 1)]
    single_host.save(destination + 'smirnoff-' + host_resname + '-unique.mol2', overwrite=True)
