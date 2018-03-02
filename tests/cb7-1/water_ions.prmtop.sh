#!/usr/bin/env bash
source $AMBERHOME/amber.sh
tleap -f water_ions.prmtop.in > leap.log
sleep 1
mv leap.log water_ions.prmtop.out