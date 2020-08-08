#!/bin/bash
# https://askubuntu.com/questions/918707/cant-change-desktop-resolution-size-1920x1080-not-found-in-available-modes

# Output generated by `cvt 1920 1080 60`
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
# Confirm "Virtual1" is connected by `xrandr --query | grep connected`
xrandr --addmode Virtual1 "1920x1080_60.00"
xrandr --output Virtual1 --mode "1920x1080_60.00" # Should automatically change display output
#unity --replace
