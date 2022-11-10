#!/usr/bin/env bash

echo "I am a test file for conditional.sh" > exists.txt
rm -i doesnotexist.txt
if [[ -a exists.txt ]]; then echo "This file exists, checked with -a"; fi
if [[ ! -e doesnotexist.txt ]]; then echo "Also works for -e too"; fi

mkdir tmp
if [[ -d tmp ]]; then echo "-d is the equivalent for directories"; fi

ln -s exists.txt LinkExist
if [[ -h LinkExist ]]; then echo "-h is for symbolic links"; fi
if [[ -L LinkExist ]]; then echo "Same with -L"; fi

echo ""
touch empty.txt
if [[ -s empty.txt ]]; then ; else echo "And since empty.txt is empty, thus -s failed"; fi

chmod -r empty.txt
if [[ -r empty.txt ]]; then ; else echo "Since empty.txt is nonreadable, -r failed"; fi
if [[ -w empty.txt ]]; then echo "But since empty.txt is writable, -w passed"; fi

echo ""
if [[ -x /bin/echo ]]; then echo "-x tests if a file/command (ie. echo) is executable"; fi

echo ""
if [[ exists.txt -ot empty.txt ]]; then echo "exists.txt is older then empty.txt\n -nt works in reverse"; fi
												
# Remove test assets
rm exists.txt
rm -rf tmp/
rm LinkExist
rm empty.txt
