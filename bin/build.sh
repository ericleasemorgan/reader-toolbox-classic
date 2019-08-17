#!/usr/bin/env bash

# build.sh - one script to rule them all


# configure
CARREL2DIAGRAM='./bin/carrel2diagram.sh'
CARREL2MODEL='./bin/carrel2model.sh'
CARREL2SEARCH='./bin/carrel2search.sh'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <short-name>" >&2
	exit
fi

# get input; initialize
CARREL=$1

# do the workk
$CARREL2DIAGRAM $CARREL &
$CARREL2MODEL   $CARREL &
$CARREL2SEARCH  $CARREL &

# hang-out and then quit
wait
exit

