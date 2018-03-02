# How to set up host-guest simulations with the SMIRNOFF99Frosst force field in AMBER
This repository contains helper functions to read AMBER-compatible simulation parameter (e.g., `prmtop`) and coordinate (e.g., `inpcrd`) files, re-parameterize those files with the SMIRNOFF99Frosst force field, and then write out parameter and coordinate files that can be used to run simulations in AMBER. Examples are given in the notebooks.

## Introduction
Changing the parameters for an already prepared host-guest complex requires a few extra steps compared to swapping the parameters for an isolated small molecule. Rather than using a SMILES string or other chemical identifier to start, the method here attempts to preserve all position and topology information (e.g., presence or absence of dummy atoms, solvation and ionization status, box vectors, and so on). There have been a few sticky spots (detailed below) that have led to some creative -- and some clunky -- workarounds; the strategy outlined below is surely not the most direct method, but it has been the most robust in my testing.

Compared with the [`smirnoff_host_guest.ipynb`](https://github.com/openforcefield/openforcefield/blob/master/examples/host_guest_simulation/smirnoff_host_guest.ipynb) example notebook, here we start with AMBER files, don't charge the molecules, don't generate 3D conformers, don't perform docking, don't solvate the structure, and don't perform any minimization.

The general method is as follows, split into three sections.

### Prepare the host and guest
1. Read in existing files<sup>*</sup> and create a standards-compliant `pdb` file.
2. Split the `pdb` into separate topologies, extracting the host and guest molecules separately.
3. Use the host and guest topologies to generate `mol2` with SYBYL atom types, polymerizing a cyclic host from a monomer, if necessary.
4. Read the host and guest `mol2` files, ensure unique atom names, and convert to OpenEye `OEMol`s.
5. Use the list of `OEMol`s to create an OpenMM system with the SMIRNOFF99Frosst force field. Since we are not running any simulations here, I don't believe the value of simulation-related options (e.g., `nonbondedCutoff=1.1 * unit.nanometer`) matter, but they are required.
6. Convert the OpenMM system into a ParmEd structure.

### Prepare the water, ions, and dummy atoms (if present)
1. Extract the water, ions, and dummy atoms (if present) from the standards-compliant `pdb` file created after reading in the existing files.
2. Parameterize the water, ions, and dummy atoms (if present) with existing force fields (e.g., TIP3P water, Joung-Cheatham monovalent ions, and so on).
3. Convert the water, ions, and dummy atoms (if present) to a ParmEd structure.

### Combine the host and guest with the water, ions, and dummy atoms (if present)
1. Add the two ParmEd structures.
2. Copy box vector information from the existing coordinates to the new coordinates.
3. If necessary (because the atom indices may change between the input and output coordinates)...
    1. Determine the mapping between atoms in the existing and new coordinate set.
    2. Determine the mapipng between residues in the existing and new coordinate set.
    3. Rewrite any restraints that have been specified using atom index or residue number masks.

<sup>*</sup> The starting point can be multiple files or one file for the whole system. In the first example notebook, the input is one pair of files for the whole system. However, in the second example notebook, the host and guest molecules each have parameters and coordinates. To set the system coordinates, a fully solvated `pdb` file is used, so this example uses five files as input.

## Testing and caveats
The included notebooks run through this workflow with two examples. First, a host-guest pair from David Mobley's [`benchmarksets`](https://github.com/mobleylab/benchmarksets) repository (CB7-memantine). Second (more challenging), input files for an existing attach-pull-release workflow, with a multi-residue host, dummy atoms, and restraints that have been to be re-encoded with new atom ordering (αCD-1-butylamine).

A few notes on things that didn't work in my testing. Many of these things might be able to work if applied in a different context or even in a different order -- and I don't want to claim they are broken -- only that these paths led to errors one way or another, in my hands. Some of the issues may be due to my unfamiliarity with the tools, but by listing them here, someone else might avoid a few pitfalls.

- Read a `mol2` file with GAFF atom types into an OpenEye `OEMol` without using `OEIFlavor_MOL2_Forcefield`. This is a huge caveat. Ignoring it can lead to [oxygen being interpreted as osmium silently](https://github.com/openforcefield/smirnoff99Frosst/issues/73), leading to incorrect parameter assignment. When wildcard assignments are eliminated, this will probably be more obvious.
- Go straight from a `prmtop` to an OpenEye `OEMol` via an OpenMM topology. This requires inferring bond orders (mentioned [here](https://github.com/openforcefield/openforcefield/issues/66#issuecomment-337696319)), which has not always worked reliably.
- Start from a `mol2` file containing host (or guest) together with water and ions. There can be unexpected results when the "Forcefield" flavor is required to parse the host (or guest). But more importantly, there is an explosion of file size when writing out a subsequent `prmtop` file, mentioned [here](https://github.com/ParmEd/ParmEd/issues/930#issuecomment-363321848).
- Try to run `createSystem` when all atoms are not unique. It's best to always run `OETriposAtomNames` to generate unique atom names. See [this](https://github.com/MobleyLab/benchmarksets/issues/64#issuecomment-349771286) issue for more information; a multi-model `mol2` seems to be troublesome, since by definition, there are non-unique atom names.
- Write a `mol2` using ParmEd after using `oemmutils` to convert an `OEMol` into an OpenMM topology. The `mol2` file won't have positions. It seems the positions are lost after running through `oemmutils`. (I have not tried to reproduce this recently.)
- Build a cyclic molecule (e.g., cyclodextrin) from SMILES and expect reasonable coordinates from OpenEye tools. I can't recall whether this is a problem building an initial structure from SMILES or even after running minimization. Other tools likely also fail to build cyclodextrin reasonably from SMILES.
- Use OpenEye to generate charges (e.g., AM1-BCC) for an entire host molecule (e.g., cyclodextrin). It will take a long time, the conformations generated are nonphysical and this may impact the quality of the charges; `antechamber` is faster and more reliable (although I don't know if it is better).
- Read a `pdb` without `CONECT` records into an `OEMol`. This is going to cause problems for determining the topology, although it is possible this could be circumvented using some combination of `OEPerceiveConnectivity` and related tools.
- Read a `pdb` with `CONECT` records between `H1` and `H2` in water. This occurs when using `trajout conect` with `cpptraj` and TIP3P water. The improper bond will either (a) prevent creation of the OpenMM system, or (b) prevent ParmEd from saving a `prmtop`. I'm not sure what determines where the error will pop up. Relatedly, this will also prevent tools like `mdtraj` from recognizing the water molecules.
- If trying to run `createSystem` will a single molecule, make sure to pass a list of `OEMol`s (i.e., a list of length 1).
- Read a `pdb` with water residue named `HOH` instead of `WAT`. This should be handled gracefully by `PDBFile` or `PDBFixer`, but I've encountered problems with solvent not being recognized as such.
- Use the option `rigidWater=True` to `createSystem()`. This is related to [this]((https://github.com/ParmEd/ParmEd/issues/930#issuecomment-363321848)) issue and can be avoided by doing the "mixed force field" approach of parameterizing the water through existing methods in AMBER, and then combining with the host and guest structure. Also, see [this](https://github.com/openforcefield/openforcefield/issues/91) and [this](https://github.com/ParmEd/ParmEd/issues/959) discussion and future developments with the new `Topology` class.
- Use OpenEye `oenb.draw_mol()` to draw a cyclic host. The molecule may look collapsed and distorted, but be sure to check with an external tool, because the coordinates may actually be okay!
- Rarely, saving a structure with ParmEd at the final step results in `AttributeError: 'NoneType' object has no attribute 'used'`, this can be [avoided](https://github.com/ParmEd/ParmEd/issues/930#issuecomment-355720672) by looping through all the bonds, but this is just a stop-gap measure, and requires further investigation. I think reading `pdb` files with `PDBFixer` is more likely to lead to this outcome.

It is also worth noting that upcoming changes to [`Topology`](https://github.com/openforcefield/openforcefield/pull/86) may address some of these issues.

## Manifest

- `build/`: Contains a `conda` environment file
- `tests/`: Directory for test case input and output
- `01-convert-benchmarkset.ipynb`: Example notebook #1 (see above)
- `02-convert-APR-files.ipynb`: Example notebook #2 (see above)
- `utils.py`: Helper functions used in the notebooks, with a few extras

## Execution
Running the notebook `01-convert-benchmarkset.ipynb` will download the input files from GitHub, switch parameters, and write the files `smirnoff.prmtop` and `smirnoff.inpcrd` in `test/cb7-1/`. Running the notebook `02-convert-APR-files.ipynb` will read files from `test/a-bam-p/original/`, switch the parameters, and write the files `smirnoff.prmtop` and `smirnoff.inpcrd` in `test/a-bam-p/generated/`

For new systems, there should be just a few places where configuration might be required:

- When using `antechamber` to write a `mol2` with SYBYL atom types, `acdoctor` may have to be [disabled](http://archive.ambermd.org/201705/0020.html) for carboxylates or other resonance structures. This is an option to `utils.convert_mol2_to_sybyl_antechamber()`
- Figuring out whethere there are dummy atoms
- Determining whether atom or residue mapping is necessary. (This process is slow, because it runs on the fully solvated system. We can't run atom mapping earlier because the atom mapping changes *after* combining the two ParmEd structures.)

### Setup
I used a custom `conda` environment to test the workflow and fix the version of `openforcefield`. The environment can be installed by running `conda env create -f build/environment.yaml`.  Note that this will install the OpenEye toolkit and requires a separate `pip` repository. For reasons that are unclear to me, 

Run the `jupyter notebook`s after activating the environment with `source activate smirnoff-host-guest`.
### Assumptions
These tools rely on AmberTools (`tleap` and `cpptraj`) to do some intermediate conversions and it is assumed the environmental variable `$AMBERHOME` is defined. This can be changed in `utils.py`. The scripts also heavily leverage OpenEye tools.