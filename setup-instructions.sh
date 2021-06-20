#!/bin/sh

#echo 'export HISTTIMEFORMAT="%d/%m/%y %T "' >> ~/.bashrc
#source ~/.bashrc

1  sudo raspi-config

12  sudo apt update
15  sudo apt full-upgrade
16  sudo apt autoremove

20  sudo apt install python3-pip
23  pip3 install virtualenv
25  python3 -m virtualenv base
27  source ./base/bin/activate

28  pip list
29  python --version
30  pip install mido
35  pip install python-rtmidi
52  sudo apt install libasound2-dev
53  sudo apt install libjack-dev

56  sudo apt install git
60  ls -la ~/.ssh
62  ssh-keygen -t ed25519 -C "xhamyd@gmail.com"
63  eval "$(ssh-agent -s)"
64  ssh-add ~/.ssh/id_ed25519
66  cat ~/.ssh/id_ed25519.pub
67  git clone git@github.com:xhamyd/dbuzzell-scripts.git
69  cd dbuzzell-scripts/
71  git status
76  git checkout -b targets/raspberrypi

80  sudo apt install emacs-nox
81  emacs setup-instructions.sh
86  history
