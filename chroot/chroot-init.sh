#!/bin/bash

function install_terminology {
    sudo apt install terminology
    gsettings set org.gnome.desktop.default-applications.terminal exec /usr/bin/terminology
    # Pretty sure this doesn't work anymore...
    #gsettings set org.gnome.desktop.default-applications.terminal exec-arg "-x"
}

function install_emacs {
    sudo apt install emacs
}

function write_aliases {
    echo -e 'alias emacs="emacs -nw"\nalias update="/usr/bin/update.sh"\nalias logout="gnome-session-quit --force"' > .bash_aliases
}

function write_update {
    echo -e 'sudo apt update\nsudo apt upgrade\nsudo apt full-upgrade\nsudo apt autoclean\nsudo apt clean\nsudo apt autoremove' | sudo tee /usr/bin/update.sh
    sudo chmod +x /usr/bin/update.sh
    # Make setup run automatically on startup!
    #   1. Go to Settings > Startup Applications
    #   2. Create new job with the following command:
    #       - `xterm -maximize -e /usr/bin/update.sh`
}

function setup_bashrc {
    install_terminology
    install_emacs
    write_aliases
    write_update
    source .bashrc
}

function y_ppa_manager {
    sudo add-apt-repository ppa:webupd8team/y-ppa-manager
    sudo apt update
    sudo apt install y-ppa-manager
}

function apt_installs {
    sudo apt install localepurge firefox fonts-lyx k4dirstat software-properties-common software-properties-gtk curl ttf-ubuntu-font-family ttf-mscorefonts-installer
    y_ppa_manager
}

function coding_installs {
    echo "Doing coding installs"
    sudo apt install python python3 default-jdk ruby-full atom puredata libreoffice
}

function music_installs {
    echo "Doing music installs"
    sudo apt install qjackctl audacity musescore
}

function gaming_installs {
    echo "Doing gaming installs"
    sudo apt install steam skypeforlinux default-jre software-centre
    echo "Go to Firefox to install: Minecraft, Adobe Flash"
    echo "Go to Software Centre to install: VBA Express"
}

function switch_on_input {
    if [ "$1" == "coding" ]; then
	coding_installs
    elif [ "$1" == "music" ]; then
	music_installs
    elif [ "$1" == "gaming" ]; then
	gaming_installs
    elif [ "$1" == "nothing" ]; then
	echo "Installing nothing extra"
    else
	echo "Use coding, music, gaming, or nothing as second parameter?"
	read -r varname
	switch_on_input "$varname"
    fi
}

function main {
    setup_bashrc
    apt_installs
    switch_on_input "$1"
    update
    echo "Make sure to add update.sh to Startup Applications!!!"
}

main "$@"
