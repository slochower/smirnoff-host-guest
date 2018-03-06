from setuptools import setup

import pathlib
import re
import subprocess

import setuptools

directory = pathlib.Path(__file__).parent.resolve()

# version
init_path = directory.joinpath('smirnoff-host-guest', '__init__.py')
text = init_path.read_text()
pattern = re.compile(r"^__version__ = ['\"]([^'\"]*)['\"]", re.MULTILINE)
version = pattern.search(text).group(1)

# long_description
readme_path = directory.joinpath('README.md')
try:
    # Try to create an reStructuredText long_description from README.md
    args = 'pandoc', '--from', 'markdown', '--to', 'rst', readme_path
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    # Fallback to markdown (unformatted on PyPI) long_description
    print('README.md conversion to reStructuredText failed. Error:')
    print(error)
    long_description = readme_path.read_text()

setuptools.setup(
    # Package details
    name='smirnovert',
    version=version,
    url='https://github.com/slochower/smirnoff-host-guest',
    description='Conversion tools for SMIRNOFF99Frosst',
    long_description=long_description,

    # Author details
    author='David Slochower',
    author_email='slochower@gmail.com',

    # Package topics
    keywords='amber smirnoff99frosst force field',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['smirnovert'],

    # Specify python version
    python_requires='>=3.6',

    # Run-time dependencies

    # I'm really not sure how to install from GitHub here without a proper egg. This could cause strange incompatibilities. This package also depends on parmed, openmm, openmoltools, openforcefield, and OpenEye tools.
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'networkx',
        'lxml',
        'requests',
    ],

    # Additional groups of dependencies
    extras_require={},
)