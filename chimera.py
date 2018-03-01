#!/usr/bin/env python
"""
Visualize AMBER restraints in UCSF Chimera.
"""

import os


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