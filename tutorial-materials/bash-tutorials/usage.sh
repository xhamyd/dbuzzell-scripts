if [[ $(id -u $(whoami)) != 0 ]]; then
    echo "Error: $0 should be run with root privileges"
    exit "$EX_USAGE";
fi

# usage
usage() {
    RET_CODE=$1;
    echo "usage: $0 -f <upgrade file>"
    echo " -f <file>  - uograde file"
    echo " -d         - do not perform actual update"
    echo " -h         - help"
    exit "$RET_CODE"
    }
