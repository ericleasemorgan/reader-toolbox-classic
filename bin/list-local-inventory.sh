#!/usr/bin/env bash

# list-local-inventory.sh - return a list of previously harvested carrels

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 7, 2020 - first cut


# configure
LIBRARY='./library'

# beautify, sort of
echo

# process each item in the library; a bit of overkill
ls $LIBRARY | sort | while read CARREL; do 	printf "$CARREL   "; done

# additional beautification and done
echo
echo
exit
