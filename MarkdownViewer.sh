#!/usr/bin/env bash

#@REQUIRES: grip and firefox to be installed

if [ -z "$1" ]; then
  MDFILE="README.md"
else
  MDFILE="$1"
fi

grip "${MDFILE}" --export viewable.html
firefox viewable.html
rm viewable.html
