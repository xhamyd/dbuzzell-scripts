#!/bin/bash

# EXAMPLE 1
# Demonstrate how read actually works
echo What cars do you like?
read car1 car2 car3
echo Your first car was: $car1
echo Your second car was: $car2
echo Your third car was: $car3

"""
user@bash: ./cars.sh
What cars do you like?
Jaguar Maserati Bentley Lotus
Your first car was: Jaguar
Your second car was: Maserati
Your third car was: Bentley Lotus
"""

# EXAMPLE 2
# Ask the user for login details
read -p 'Username: ' uservar #prompt
read -sp 'Password: ' passvar #silent-prompt
echo
echo Thank you $uservar we now have your login details

"""
user@bash: ./login.sh
Username: ryan
Password: 
Thank you ryan we now have your login details
"""

