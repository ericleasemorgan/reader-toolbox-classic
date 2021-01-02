#!/usr/bin/env python

# geolocate.py - given a place, return geolocation data/information

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 4, 2020 - first documentation with consultation with Matt Simpson; needs to check for API key(s)


# configure
MAXROWS        = 3
USERNAME       = 'ericleasemorgan'
FEATURECLASSES = [ 'A', 'P' ]

# require
import geocoder
import sys

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <place>\n" )
	quit()

# get input
place = sys.argv[ 1 ]

# find all places and loop through them
results = geocoder.geonames( place, name_startsWith=place, key=USERNAME, maxRows=MAXROWS, featureClass=FEATURECLASSES )
for result in results:

	# get details
	details = geocoder.geonames( result.geonames_id, method='details', key=USERNAME )
	lat               = details.lat
	lng               = details.lng
	country           = details.country
	state             = details.state
	status            = details.status
	feature_class     = details.feature_class
	class_description = details.class_description
	continent         = details.continent
	url               = details.wikipedia

	# output and done
	if status == 'OK' : print( "^".join( [ feature_class, class_description, continent, state, country, str(lat), str(lng), url ] ) )

exit