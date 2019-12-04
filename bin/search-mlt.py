#!/usr/bin/env python

# search-mlt.py - given a text and a paragraph's identifier, return additional relavant (TFIDF) paragraphs

# Eric Lease Morgan <emorgan@nd.edu>
# March 20, 2018 - first investigations; weird


# configure
MAXIMUM = 5
DEBUG   = 0

# require
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise        import cosine_similarity
import operator
import re
import sys

# sanity check
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <file> <identifier>\n" )
	quit()

# get input
book = sys.argv[ 1 ]
key  = int( sys.argv[ 2 ] )

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

# output the index, if desired
if DEBUG > 0 : 
	for i in range( 0, len( index ) ) : print( "%s\t%s\n" % ( i, index[ i ] ) )
	quit()
	
# vectorize the input and compute similarities, all in two go'es
tfidf        = TfidfVectorizer( input=index.values(), stop_words="english", ngram_range=( 1, 2 ) )
similarities = cosine_similarity( tfidf.fit_transform( index.values() ) )

# echo the given document
print( "  %s - %s\n\n" % ( key, index[ key ] ) )

# get all the similar documents to a given document
similarities = similarities[ key ]

# output similar documents limited by MAXIMUM, and done
for i in similarities.argsort()[ MAXIMUM * -1 - 1 : -1 ] : print( "  %s - %s\n" % ( i, index[ i ] ) )
quit()	
	