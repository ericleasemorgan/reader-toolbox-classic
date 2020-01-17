#!/usr/bin/env bash


QUERY='.mode tabs\nselect count(entity) as c, entity from ent where type is "GPE" group by entity order by c desc;'
DB='./jobs/etc/reader.db'
GEOCODER='./coder.py'

echo -e "COUNT\tPLACE\tADDRESS\tQUALITY\tSTATE\tSTATUS\tLAT\tLNG"

printf "$QUERY" | sqlite3 $DB | while read COUNT PLACE; do

	if [[ $COUNT > 3 ]]; then
	
		RESULT=$( $GEOCODER "$PLACE" )

		ADDRESS=$( echo $RESULT | cut -d ^ -f1 ) 
		QUALITY=$( echo $RESULT | cut -d ^ -f2 ) 
		STATE=$( echo $RESULT | cut -d ^ -f3 ) 
		STATUS=$( echo $RESULT | cut -d ^ -f4 ) 
		LAT=$( echo $RESULT | cut -d ^ -f5 ) 
		LNG=$( echo $RESULT | cut -d ^ -f6 ) 
		
		echo -e "$COUNT\t$PLACE\t$ADDRESS\t$QUALITY\t$STATE\t$STATUS\t$LAT\t$LNG"
		
	fi

done
exit