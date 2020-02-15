#!/bin/bash

cmd="ls /usr/bin"

# greps "grep" at the back of the word
ls /usr/bin | grep "grep$"

# grep "ip" in the front
ls /usr/bin | grep ^ip

ls /usr/bin | grep ^net

#One liner
-e append stuff for grep 
$cmd | grep "grep$" && $cmd | grep ^ip | grep ^net
