#!/bin/bash
for (( i = 30; i < 38; i++ )); do
    echo -e "\033[0;"$i"m Normal: (0,$i); \033[1;"$i"m Light: (1;$i)";
done
