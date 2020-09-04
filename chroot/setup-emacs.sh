#!/bin/bash

# Install Emacs in ChromeOS Shell
#@REQUIRES: Dev mode enabled, to enter crosh shell
sudo su -
dev_install
emerge qemacs
