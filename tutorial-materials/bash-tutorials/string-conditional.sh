#!/usr/bin/env bash

if [[ -z "" ]]; then
	echo "Blank string is empty; checked with -z"
fi

if [[ -n "non-empty" ]]; then
	echo "-n for non-empty strings"
	echo "(though the string itself without any flags would also work"
fi

if [[ "first_string" == "second_string" ]]; then
	echo "ERROR: Something's broken..."
else
	echo "== is for string equality, != is for string inequality"
fi

if [[ "abc" < "bcd" ]]; then
	echo "< is for alphabetical ordering"
	echo "< - before alphabetically"
	echo "> - after alphabetically"
fi


																								 
