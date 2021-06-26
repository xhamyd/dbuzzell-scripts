#!/bin/bash

sudo true  # Blank command for the password prompt
echo "APT updates..."
sudo apt -qq update -y
#sudo apt -qq upgrade -y  # full-upgrade does more, learned from the RPi community
sudo apt -qq full-upgrade -y
#sudo apt -qq autoclean -y
#sudo apt -qq clean -y
sudo apt -qq autoremove -y
echo ""
#@NOTE: Everyone's pip setup is different, not automatically doing this
# echo "Upgrading pip..."
# pip -q install --upgrade pip
# echo ""
echo "Update snaps..."
sudo snap refresh
