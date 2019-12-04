#!/usr/bin/env bash

# db2malletcsv.sh - given a carrel name, output a CSV metadata file suitable for Topic Model Tool


# configure
SQL=".mode csv\n.headers on\nSELECT id || '.txt' AS id, author FROM bib ORDER BY author;"

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi

# get input
CARREL=$1

# do the work and done
printf "$SQL" | sqlite3 "./library/$CARREL/etc/reader.db"
exit
