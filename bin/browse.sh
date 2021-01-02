#!/usr/bin/env bash

# browse.sh - given the name of a carrel, read the HTML report

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# December 23, 2020 - first cut; at the cabin


# configure
READER_HOME='/Users/eric/Documents/reader-toolbox'

if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi

CARREL=$1
HTML="$READER_HOME/library/$CARREL/index.htm"
lynx $HTML
exit

