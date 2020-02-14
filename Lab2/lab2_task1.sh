#!/bin/bash

num_writer() {
	if [ "$#" -lt 1 ]; then
		usage
	elif [ "$#" -eq 1 ]; then
		echo "We have one input"
		shuf -i 1-32767 -n $1 > rands_$1.txt
		small=$(cat rands_$1.txt | sort -n | head -n 1)
		large=$(cat rands_$1.txt | sort -n | tail -n 1)
		echo "You requested $1 numbers"
		echo "The smallest value generated was $small"
		echo "The largest value generated was $large"
		echo "The average value generated was $average"
	elif [ "$#" -eq 3 ]; then
		echo "THeree"
	else
		echo "Too much arguments. Bye!!!"
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

#shuf -i 0-50 -n $num_rands
#for ((i=1; i <= $num_rands; i++))
#do
#	echo $i
#	shuf -i 0-50 -n $i
#done

