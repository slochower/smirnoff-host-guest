#!/usr/bin/env bash
source $AMBERHOME/amber.sh
tleap -f water_ions.prmtop.in > leap.log
mv leap.log water_ions.prmtop.out