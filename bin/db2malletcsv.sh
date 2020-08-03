#!/usr/bin/env bash

# db2malletcsv.sh - given a carrel name, output a CSV metadata file suitable for Topic Model Tool

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 3, 2020 - first documentation


# configure
SQL=".mode csv\n.headers on\nSELECT id || '.txt' AS id, ##FIELD## FROM bib order by ##FIELD##;"
LIBRARY='./library'

# sanity check
if [[ -z $1 || -z $2 ]]; then
	echo "Usage: $0 <carrel> <author|title|date>\n" >&2
	exit
fi

# get input
CARREL=$1
FIELD=$2

# build the sql	
SQL=$( echo "$SQL" | sed "s/##FIELD##/$FIELD/g" )

# do the work and done
printf "$SQL" | sqlite3 "$LIBRARY/$CARREL/etc/reader.db"
exit
