#!/usr/bin/env bash
set -e

source $AMBERHOME/amber.sh
pmemd -O -p solvated_smirnoff.prmtop -ref solvated_smirnoff.inpcrd -c solvated_smirnoff.inpcrd -i mini.in -o mini.out -r mini.rst -inf /dev/null
pmemd.cuda -O -p solvated_smirnoff.prmtop -ref solvated_smirnoff.inpcrd -c mini.rst -i therm1.in -o therm1.out -r therm1.rst -inf therm1.mdinfo
pmemd.cuda -O -p solvated_smirnoff.prmtop -ref solvated_smirnoff.inpcrd -c therm1.rst -i therm2.in -o therm2.out -r therm2.rst -inf therm2.mdinfo
cp therm2.rst eqnpt.001.rst
pmemd.cuda -O -p solvated_smirnoff.prmtop -ref solvated_smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.001.out -r eqnpt.001.rst -inf /dev/null >& eqnpt.log

