#!/bin/bash

sudo apt -qq update -y
sudo apt -qq upgrade -y
#sudo apt full-upgrade -y
#sudo apt autoclean -y
#sudo apt clean -y
sudo apt -qq autoremove -y
