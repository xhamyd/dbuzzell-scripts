#!/usr/bin/env bash

# EXAMPLE 1
# Replace text in place, for a progress bar effect
echo -ne "#   1\r"
sleep 1
echo -ne "##  2\r"
sleep 1
echo -ne "### 3\r"
echo -ne "\n"

# EXAMPLE 2
# Silence output using /dev/null
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
