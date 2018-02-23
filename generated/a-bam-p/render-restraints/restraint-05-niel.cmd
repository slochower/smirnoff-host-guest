sleep 1
~display :WAT
~display :Na+
turn y 90
color grey
color red @/serialNumber=1
repr bs @/serialNumber=1
color red @/serialNumber=13
repr bs @/serialNumber=13
color red @/serialNumber=46
repr bs @/serialNumber=46
color red @/serialNumber=104
repr bs @/serialNumber=104
2dlabel create title text "1,13,46,104," xpos 0.1 ypos 0.92 color black
copy file restraint-05-niel.png
stop