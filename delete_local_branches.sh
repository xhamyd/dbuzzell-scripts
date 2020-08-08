#!/bin/bash

# Option 1: Remove tracking branches not on origin
git remote prune origin

# Option 2: Remove branches that have been deleted on origin
# Source: https://stackoverflow.com/a/38404202
git checkout master
git fetch -p
git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d

# Option 3: Choose which merged branches to delete
# Source: https://stackoverflow.com/a/28464339
git branch --merged > /tmp/merged-branches
nano /tmp/merged-branches  # Remove branch names not to be deleted
xargs git branch -d < /tmp/merged-branches
