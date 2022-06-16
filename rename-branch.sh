#!/bin/bash

old_name="$(git rev-parse --abbrev-ref HEAD)"
new_name="$1"

git branch -m "$new_name"
git push origin -u "$new_name"
git push origin --delete "$old_name"
