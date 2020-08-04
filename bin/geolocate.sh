#!/usr/bin/env bash

# geolocate.sh - given a carrel, output TSV stream of geolocations ; a front-end to geolocate.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 4, 2020 - first documentation; need to check for API key(s)


# configure
QUERY='.mode tabs\nselect count(entity) as c, entity from ent where type is "GPE" group by entity order by c desc;'
DB='etc/reader.db'
LIBRARY='./library'
GEOLOCATE='./bin/geolocate.py'
MINIMUM=5

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi

# get input
CARREL=$1

# output header
echo -e "COUNT\tPLACE\tCLASS\tDESCRIPTION\tCONTINENT\tSTATE\tCOUNTRY\tLAT\tLNG\tURL"

# process each location
printf "$QUERY" | sqlite3 "$LIBRARY/$CARREL/$DB" | while read COUNT PLACE; do

	# only process "frequently occurring" places
	if [[ $COUNT > $MINIMUM ]]; then
	
		# debug
		echo -e "$COUNT\t$PLACE" >&2
		
		# geolocate
		RESULT=$( $GEOLOCATE "$PLACE" )

		# parse
		CLASS=$( echo $RESULT       | cut -d ^ -f1 ) 
		DESCRIPTION=$( echo $RESULT | cut -d ^ -f2 ) 
		CONTINENT=$( echo $RESULT   | cut -d ^ -f3 ) 
		STATE=$( echo $RESULT       | cut -d ^ -f4 ) 
		COUNTRY=$( echo $RESULT     | cut -d ^ -f5 ) 
		LAT=$( echo $RESULT         | cut -d ^ -f6 ) 
		LNG=$( echo $RESULT         | cut -d ^ -f7 ) 
		URL=$( echo $RESULT         | cut -d ^ -f8 ) 
		
		# output
		echo -e "$COUNT\t$PLACE\t$CLASS\t$DESCRIPTION\t$CONTINENT\t$STATE\t$COUNTRY\t$LAT\t$LNG\t$URL"

		
	fi

# fini
done
exit