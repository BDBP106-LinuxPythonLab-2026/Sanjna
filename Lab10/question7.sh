#!/bin/bash
# Getting the username of the logged-in user
logged_in_user=$(whoami)
# Checking if the user is logged in
if [ -n "$logged_in_user" ];
# spell-check "logged" and adding a "]" instead of a ")"
then
echo "The logged-in user is: $logged_in_user"
# changing the "-" to "_" and lowercase "USER"
else
echo "User is not logged in"
fi


