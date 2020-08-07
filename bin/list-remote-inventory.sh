#!/usr/bin/env bash

# list-remote-inventory.sh - return a list of items available for harvesting from a remote collection

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 7, 2020 - first cut


# configure
INVENTORY='http://52.188.175.42/etc/table.tsv'

# beautify, sort of
echo

# process each item in the inventory
wget -q -O - $INVENTORY | sort | while read RECORD; do

	# parse and output
	CARREL=$( echo $RECORD | cut -d' ' -f1 )
	printf "$CARREL   "

done

# additional beautification and done
echo
echo
exit
