#!/bin/bash

# The ':' symbol denotes a no-op
if [ -z $1 ]; do
    my_function
else
    :
fi

# Similar operations
if [ -z $1 ]; do
    my_function
else
    true    # Exit code: SUCCESS
    #false  # Exit code: FAILURE
fi
