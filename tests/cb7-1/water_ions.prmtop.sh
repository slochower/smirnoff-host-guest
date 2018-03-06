#!/usr/bin/env bash
tleap -f water_ions.prmtop.in && sleep 1
mv leap.log water_ions.prmtop.out