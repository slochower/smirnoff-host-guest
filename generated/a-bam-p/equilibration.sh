#!/usr/bin/env bash
source $AMBERHOME/amber.sh
pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c smirnoff.inpcrd -i mini.in -o mini.out -r mini.rst -inf /dev/null
pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c mini.rst -i therm1.in -o therm1.out -r therm1.rst -inf therm1.mdinfo
pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c therm1.rst -i therm2.in -o therm2.out -r therm2.rst -inf therm2.mdinfo
cp therm2.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.01.out -r eqnpt.01.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.01.out >> eqnpt.all.out
cp eqnpt.01.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.02.out -r eqnpt.02.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.02.out >> eqnpt.all.out
cp eqnpt.02.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.03.out -r eqnpt.03.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.03.out >> eqnpt.all.out
cp eqnpt.03.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.04.out -r eqnpt.04.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.04.out >> eqnpt.all.out
cp eqnpt.04.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.05.out -r eqnpt.05.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.05.out >> eqnpt.all.out
cp eqnpt.05.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.06.out -r eqnpt.06.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.06.out >> eqnpt.all.out
cp eqnpt.06.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.07.out -r eqnpt.07.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.07.out >> eqnpt.all.out
cp eqnpt.07.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.08.out -r eqnpt.08.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.08.out >> eqnpt.all.out
cp eqnpt.08.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.09.out -r eqnpt.09.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.09.out >> eqnpt.all.out
cp eqnpt.09.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.10.out -r eqnpt.10.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.10.out >> eqnpt.all.out
cp eqnpt.10.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.11.out -r eqnpt.11.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.11.out >> eqnpt.all.out
cp eqnpt.11.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.12.out -r eqnpt.12.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.12.out >> eqnpt.all.out
cp eqnpt.12.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.13.out -r eqnpt.13.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.13.out >> eqnpt.all.out
cp eqnpt.13.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.14.out -r eqnpt.14.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.14.out >> eqnpt.all.out
cp eqnpt.14.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.15.out -r eqnpt.15.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.15.out >> eqnpt.all.out
cp eqnpt.15.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.16.out -r eqnpt.16.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.16.out >> eqnpt.all.out
cp eqnpt.16.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.17.out -r eqnpt.17.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.17.out >> eqnpt.all.out
cp eqnpt.17.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.18.out -r eqnpt.18.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.18.out >> eqnpt.all.out
cp eqnpt.18.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.19.out -r eqnpt.19.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.19.out >> eqnpt.all.out
cp eqnpt.19.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.20.out -r eqnpt.20.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.20.out >> eqnpt.all.out
cp eqnpt.20.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.21.out -r eqnpt.21.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.21.out >> eqnpt.all.out
cp eqnpt.21.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.22.out -r eqnpt.22.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.22.out >> eqnpt.all.out
cp eqnpt.22.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.23.out -r eqnpt.23.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.23.out >> eqnpt.all.out
cp eqnpt.23.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.24.out -r eqnpt.24.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.24.out >> eqnpt.all.out
cp eqnpt.24.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.25.out -r eqnpt.25.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.25.out >> eqnpt.all.out
cp eqnpt.25.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.26.out -r eqnpt.26.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.26.out >> eqnpt.all.out
cp eqnpt.26.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.27.out -r eqnpt.27.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.27.out >> eqnpt.all.out
cp eqnpt.27.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.28.out -r eqnpt.28.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.28.out >> eqnpt.all.out
cp eqnpt.28.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.29.out -r eqnpt.29.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.29.out >> eqnpt.all.out
cp eqnpt.29.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.30.out -r eqnpt.30.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.30.out >> eqnpt.all.out
cp eqnpt.30.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.31.out -r eqnpt.31.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.31.out >> eqnpt.all.out
cp eqnpt.31.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.32.out -r eqnpt.32.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.32.out >> eqnpt.all.out
cp eqnpt.32.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.33.out -r eqnpt.33.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.33.out >> eqnpt.all.out
cp eqnpt.33.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.34.out -r eqnpt.34.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.34.out >> eqnpt.all.out
cp eqnpt.34.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.35.out -r eqnpt.35.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.35.out >> eqnpt.all.out
cp eqnpt.35.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.36.out -r eqnpt.36.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.36.out >> eqnpt.all.out
cp eqnpt.36.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.37.out -r eqnpt.37.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.37.out >> eqnpt.all.out
cp eqnpt.37.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.38.out -r eqnpt.38.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.38.out >> eqnpt.all.out
cp eqnpt.38.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.39.out -r eqnpt.39.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.39.out >> eqnpt.all.out
cp eqnpt.39.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.40.out -r eqnpt.40.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.40.out >> eqnpt.all.out
cp eqnpt.40.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.41.out -r eqnpt.41.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.41.out >> eqnpt.all.out
cp eqnpt.41.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.42.out -r eqnpt.42.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.42.out >> eqnpt.all.out
cp eqnpt.42.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.43.out -r eqnpt.43.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.43.out >> eqnpt.all.out
cp eqnpt.43.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.44.out -r eqnpt.44.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.44.out >> eqnpt.all.out
cp eqnpt.44.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.45.out -r eqnpt.45.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.45.out >> eqnpt.all.out
cp eqnpt.45.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.46.out -r eqnpt.46.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.46.out >> eqnpt.all.out
cp eqnpt.46.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.47.out -r eqnpt.47.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.47.out >> eqnpt.all.out
cp eqnpt.47.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.48.out -r eqnpt.48.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.48.out >> eqnpt.all.out
cp eqnpt.48.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.49.out -r eqnpt.49.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.49.out >> eqnpt.all.out
cp eqnpt.49.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.50.out -r eqnpt.50.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.50.out >> eqnpt.all.out
cp eqnpt.50.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.51.out -r eqnpt.51.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.51.out >> eqnpt.all.out
cp eqnpt.51.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.52.out -r eqnpt.52.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.52.out >> eqnpt.all.out
cp eqnpt.52.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.53.out -r eqnpt.53.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.53.out >> eqnpt.all.out
cp eqnpt.53.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.54.out -r eqnpt.54.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.54.out >> eqnpt.all.out
cp eqnpt.54.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.55.out -r eqnpt.55.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.55.out >> eqnpt.all.out
cp eqnpt.55.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.56.out -r eqnpt.56.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.56.out >> eqnpt.all.out
cp eqnpt.56.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.57.out -r eqnpt.57.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.57.out >> eqnpt.all.out
cp eqnpt.57.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.58.out -r eqnpt.58.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.58.out >> eqnpt.all.out
cp eqnpt.58.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.59.out -r eqnpt.59.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.59.out >> eqnpt.all.out
cp eqnpt.59.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.60.out -r eqnpt.60.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.60.out >> eqnpt.all.out
cp eqnpt.60.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.61.out -r eqnpt.61.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.61.out >> eqnpt.all.out
cp eqnpt.61.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.62.out -r eqnpt.62.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.62.out >> eqnpt.all.out
cp eqnpt.62.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.63.out -r eqnpt.63.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.63.out >> eqnpt.all.out
cp eqnpt.63.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.64.out -r eqnpt.64.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.64.out >> eqnpt.all.out
cp eqnpt.64.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.65.out -r eqnpt.65.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.65.out >> eqnpt.all.out
cp eqnpt.65.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.66.out -r eqnpt.66.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.66.out >> eqnpt.all.out
cp eqnpt.66.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.67.out -r eqnpt.67.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.67.out >> eqnpt.all.out
cp eqnpt.67.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.68.out -r eqnpt.68.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.68.out >> eqnpt.all.out
cp eqnpt.68.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.69.out -r eqnpt.69.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.69.out >> eqnpt.all.out
cp eqnpt.69.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.70.out -r eqnpt.70.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.70.out >> eqnpt.all.out
cp eqnpt.70.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.71.out -r eqnpt.71.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.71.out >> eqnpt.all.out
cp eqnpt.71.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.72.out -r eqnpt.72.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.72.out >> eqnpt.all.out
cp eqnpt.72.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.73.out -r eqnpt.73.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.73.out >> eqnpt.all.out
cp eqnpt.73.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.74.out -r eqnpt.74.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.74.out >> eqnpt.all.out
cp eqnpt.74.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.75.out -r eqnpt.75.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.75.out >> eqnpt.all.out
cp eqnpt.75.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.76.out -r eqnpt.76.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.76.out >> eqnpt.all.out
cp eqnpt.76.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.77.out -r eqnpt.77.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.77.out >> eqnpt.all.out
cp eqnpt.77.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.78.out -r eqnpt.78.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.78.out >> eqnpt.all.out
cp eqnpt.78.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.79.out -r eqnpt.79.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.79.out >> eqnpt.all.out
cp eqnpt.79.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.80.out -r eqnpt.80.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.80.out >> eqnpt.all.out
cp eqnpt.80.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.81.out -r eqnpt.81.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.81.out >> eqnpt.all.out
cp eqnpt.81.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.82.out -r eqnpt.82.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.82.out >> eqnpt.all.out
cp eqnpt.82.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.83.out -r eqnpt.83.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.83.out >> eqnpt.all.out
cp eqnpt.83.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.84.out -r eqnpt.84.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.84.out >> eqnpt.all.out
cp eqnpt.84.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.85.out -r eqnpt.85.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.85.out >> eqnpt.all.out
cp eqnpt.85.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.86.out -r eqnpt.86.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.86.out >> eqnpt.all.out
cp eqnpt.86.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.87.out -r eqnpt.87.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.87.out >> eqnpt.all.out
cp eqnpt.87.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.88.out -r eqnpt.88.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.88.out >> eqnpt.all.out
cp eqnpt.88.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.89.out -r eqnpt.89.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.89.out >> eqnpt.all.out
cp eqnpt.89.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.90.out -r eqnpt.90.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.90.out >> eqnpt.all.out
cp eqnpt.90.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.91.out -r eqnpt.91.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.91.out >> eqnpt.all.out
cp eqnpt.91.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.92.out -r eqnpt.92.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.92.out >> eqnpt.all.out
cp eqnpt.92.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.93.out -r eqnpt.93.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.93.out >> eqnpt.all.out
cp eqnpt.93.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.94.out -r eqnpt.94.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.94.out >> eqnpt.all.out
cp eqnpt.94.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.95.out -r eqnpt.95.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.95.out >> eqnpt.all.out
cp eqnpt.95.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.96.out -r eqnpt.96.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.96.out >> eqnpt.all.out
cp eqnpt.96.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.97.out -r eqnpt.97.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.97.out >> eqnpt.all.out
cp eqnpt.97.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.98.out -r eqnpt.98.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.98.out >> eqnpt.all.out
cp eqnpt.98.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.99.out -r eqnpt.99.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.99.out >> eqnpt.all.out
cp eqnpt.99.rst eqnpt.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c eqnpt.rst -i eqnpt.in -o eqnpt.100.out -r eqnpt.100.rst -inf /dev/null >& eqnpt.log 
cat eqnpt.100.out >> eqnpt.all.out
cp eqnpt.100.rst eqnpt.rst

