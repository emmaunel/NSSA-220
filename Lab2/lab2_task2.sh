#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
	exit 1
fi

function user_input() {
    read -p 'Username: ' user
    read -p 'Full Name: ' fullname
    read -p 'Department: ' depar
    read -p 'Job Title: ' job
}

function file_system_writer() {
	mkdir -p /home/$1/{Desktop,Documents,Downloads,Pictures}
}

function letter_writer() {
	cat << EOF > /home/$1/Desktop/welcome.txt
Dear $fullname,
	
Welcome to Initech Corportation! We're so happy to have you
in the $depar Department as a $job. Pleae don't forgot to 
complete your TPS Reports in a timely manner.

Sincerely,
Bill Lumbergh
EOF
	cp ackbar.png /home/$1/Pictures/ackbar.png
} 

function permission_editor() {
	echo "Changing Permission"
	chown -R $1:$1 /home/$1	
}

function letbetogether() {
	echo "Creating Directory for $1"
	file_system_writer $1
	letter_writer $1
	permission_editor $1
}

user_input
echo
useradd $user
echo "User $user added!"
letbetogether $user

read -p 'Would you like to add another user?(y/n):' option

while [ $option == 'y' ]; do
	user_input
	echo
	useradd $user
	echo "User $user added!"
	letbetogether $user
	read -p 'Would you like to add another user?(y/n):' option
done

echo "Thank you! Have a nice day"
