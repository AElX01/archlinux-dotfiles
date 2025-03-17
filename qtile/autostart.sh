#!/usr/bin/env sh 

picom -b # run picom 

# -- randomize mac address
macchanger -r wlo1 
macchanger -r enp2s0

nm-applet & # nm-applet systray
