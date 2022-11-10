#!/usr/bin/env bash

SILENT=false

function print_something {
	if [[ "$1" == "--silent" ]]; then
		SILENT=true
	fi

	OUTPUT="here's some fancy output, unquietted"
	if "$SILENT"; then
		echo $OUTPUT &>/dev/null
	else
		echo $OUTPUT
	fi
}		

print_something $1
