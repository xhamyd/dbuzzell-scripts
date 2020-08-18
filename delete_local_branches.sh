#!/bin/bash

if [[ -z "$1" || "$1" == 1 ]]; then
    # Option 1: Remove tracking branches not on origin
    git remote prune origin
elif [[ "$1" == 2 ]]; then
    # Option 2: Remove branches that have been deleted on origin
    # Source: https://stackoverflow.com/a/38404202
    git checkout master
    git fetch -p
    git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d
elif [[ "$1" == 3 ]]; then
    # Option 3: Choose which merged branches to delete
    # Source: https://stackoverflow.com/a/28464339
    git branch --merged > /tmp/merged-branches
    nano /tmp/merged-branches  # Remove branch names not to be deleted
    xargs git branch -d < /tmp/merged-branches
else
    echo "Option not supported, please submit with '1' (default), '2', or '3'"
fi
