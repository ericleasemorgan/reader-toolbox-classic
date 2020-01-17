#!/usr/bin/env python

import geocoder
import sys

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <place>\n" )
	quit()

# get input
place = sys.argv[ 1 ]

# do the work, output, and done
g = geocoder.google( place )

# parse
address = g.address
lat     = g.lat
lng     = g.lng
quality = g.quality
state   = g.state
status  = g.status

# output and done
if status == 'OK' : print( "^".join( [ str(address), str(quality), str(state), str(status), str(lat), str(lng) ] ) )
exit