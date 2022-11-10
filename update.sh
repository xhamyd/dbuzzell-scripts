#!/usr/bin/env bash

case "$1" in
    "apt")
        "${DBUZZELL_SCRIPTS}"/aupdate.sh
        ;;
    "git")
        "${DBUZZELL_SCRIPTS}"/gupdate.sh
        ;;
    "")
        "${DBUZZELL_SCRIPTS}"/aupdate.sh
        echo ""
        "${DBUZZELL_SCRIPTS}"/gupdate.sh
        ;;
    *)
        echo "Invalid arg provided: $1"
        ;;
esac
