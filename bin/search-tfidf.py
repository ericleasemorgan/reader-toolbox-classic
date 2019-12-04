#!/usr/bin/env python

# search-tfidf.py - given a text and a query, return a pre-configured number of most relavant (TFIDF) paragraphs

# Eric Lease Morgan <emorgan@nd.edu>
# March 20, 2018 - first cut, and hard work; Happy Spring!


# configure
MAXIMUM = 5

# require
from sklearn.feature_extraction.text import TfidfVectorizer
import operator
import re
import sys

# sanity check
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <file> <query>\n" )
	quit()

# get input
book  = sys.argv[ 1 ]
query = sys.argv[ 2 ].lower()

# open the book and parse it into paragraphs
handle     = open( book, 'r' )
book       = handle.read()
paragraphs = book.split( "\n\n" )

# index normalized paragraphs
index = {}
for i in range ( 0, len( paragraphs ) ) :
	text       = paragraphs[ i ].lower()
	text       = text.replace( '\n', ' ' )
	text       = re.sub( '^ +', '', text )
	index[ i ] = text

# vectorize the input and extract the resulting vocabulary
tfidf        = TfidfVectorizer( input=index.values(), stop_words="english" )
matrix       = tfidf.fit_transform( index.values() )
vocabulary   = tfidf.vocabulary_

# initialize search results
hits = {}

# loop through each item in the index; there has got to be a better way
for i in range( 0, len( index ) ) :
	
	# get document and it indexes
	document = matrix[ i ]
	indices  = document.indices
	scores   = document.data
	
	# loop through each word in the index
	for j in range ( 0, len( indices ) ) :
		
		# if the word matches the query, then update list of hits
		if indices[ j ] == vocabulary[ query ] : hits[ i ] = scores[ j ]

# sort the hits; returns tuples
hits = sorted( hits.items(), key=operator.itemgetter( 1 ), reverse=True )

# process each hit
for i in range( 0, len( hits ) ) :
	key      = hits[ i ][ 0 ]
	document = index[ key ]
	print( "  %s - %s\n" % ( key, document ) )
	if i == MAXIMUM : break

# done
quit()

	
	