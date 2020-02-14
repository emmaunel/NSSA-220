#!/bin/bash

num_writer() {
	if [ "$#" -lt 1 ]; then
		usage
	elif [ "$#" -eq 1 ]; then
		shuf -i 1-32767 -n $1 > rands_$1.txt
		small=$(cat rands_$1.txt | sort -n | head -n 1)
		large=$(cat rands_$1.txt | sort -n | tail -n 1)
		echo "You requested $1 numbers"
		echo "The smallest value generated was $small"
		echo "The largest value generated was $large"
		average=0;
		while read line; do
			average=$(($average + $line))
		done < rands_$1.txt
		echo "The average value generated was $average"
	elif [ "$#" -eq 3 ]; then
		shuf -i $2-$3 -n $1 > rands_$1.txt
		small=$(cat rands_$1.txt | sort -n | head -n 1)
		large=$(cat rands_$1.txt | sort -n | tail -n 1)
		echo "You requested $1 numbers"
		echo "The smallest value generated was $small"
		echo "The largest value generated was $large"
		average=0;
		while read line; do
			average=$(($average + $line))
		done < rands_$1.txt
		echo "The average value generated was $average"
	fi
}	

function usage() {
	echo "./lab2_task1.sh <required> <optional> <optional>"
	exit 1
}

num_rands=$1
min=$2
max=$3

num_writer $num_rands $min $max