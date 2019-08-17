#!/usr/bin/env bash

# template2html.sh - given the short name of a Distant Reader study carrel, output an HTML file containing a topic modeling interface

# Eric Lease Morgan <emorgan@nd.edu>
# August 7, 2019 - first documentation, and based on the good work of Team JAMS (Aarushi Bisht, Cheng Jial, Mel Mashiku, and Shivam Rastogi)


# configure
TEMPLATE='./etc/template-model.htm'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi

# get input
CARREL=$1

# do the work, output, and done
HTML=$( cat $TEMPLATE | sed "s/##CARREL##/$CARREL/g" )
echo $HTML
