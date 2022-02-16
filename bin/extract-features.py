#!/usr/bin/env python

# extract.py - given a carrel and a type, return a list of features

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# January 5, 2021 - first investigations; textacy++


# configure
LIBRARY = './library/'
CORPUS  = '/etc/reader.txt'
PICKLE  = '/etc/reader.bin'
MODEL   = 'en_core_web_sm'

# require
import sys
import os
import os.path
import textacy
import spacy

# usage
def usage() :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <carrel> <svo|sss|noun-chunks|quotations>\n" )
	quit()

# given a carrel, return a spacy doc
def carrel2doc( carrel ) :

	# initialize
	pickle = LIBRARY + carrel + PICKLE
	
	# check to see if we've previously been here
	if os.path.exists( pickle ) :
			
		# read the picke file
		doc = next( textacy.io.spacy.read_spacy_docs( pickle ) )
		
	# otherwise
	else :
		
		# warn
		sys.stderr.write( 'Reading and formatting data for future use. This may take many minutes. Please be patient...\n' )

		# create a doc
		file = LIBRARY + carrel + CORPUS
		text = open( file ).read()
		size = ( os.stat( file ).st_size ) + 1
		nlp  = spacy.load( MODEL, max_length=size )
		doc  = nlp( text )
	
		# save it for future use
		textacy.io.spacy.write_spacy_docs( doc, filepath=pickle )
	
	# done
	return doc


# sanity check
if len( sys.argv ) < 3 : usage()

# get input
carrel  = sys.argv[ 1 ]
feature = sys.argv[ 2 ]

# subjects-verbs-objects
if feature == 'svo' :
	
	# initialize
	doc = carrel2doc( carrel )
	
	# get the features
	features = list( textacy.extract.subject_verb_object_triples( doc ) )
	
	# process each one
	for feature in features : 
		
		# parse and output
		subject = feature[ 0 ].text
		verb    = feature[ 1 ].text
		object  = feature[ 2 ].text

		# output
		print( "\t".join( ( subject, verb, object ) ) )
	
# noun chunks
elif feature == 'noun-chunks' :

	# initialize
	doc = carrel2doc( carrel )
	
	# get the features
	features = list( textacy.extract.noun_chunks( doc ) )

	# process each one
	for feature in features : 
		
		# parse and output
		chunk = feature.text

		# output
		print( chunk )
	
# semistructured statements
elif feature == 'sss' :

	# get additional input
	entity = sys.argv[ 3 ]
	cue    = sys.argv[ 4 ]
	
	# initialize
	doc = carrel2doc( carrel )
	
	# get the features
	features = list( textacy.extract.semistructured_statements( doc, entity=entity, cue=cue ) )

	# process each one
	for feature in features : 
		
		# parse and output
		entity   = feature[ 0 ].text
		cue      = feature[ 1 ].text
		fragment = feature[ 2 ].text

		# output
		print( "\t".join( ( entity, cue, fragment ) ) )
	
# direct quotes
elif feature == 'quotations' :

	# initialize
	doc = carrel2doc( carrel )
	
	# get the features
	features = list( textacy.extract.direct_quotations( doc ) )
	
	# process each one
	for feature in features : 
		
		# parse and output
		speaker   = feature[ 0 ].text
		verb      = feature[ 1 ].text
		quotation = feature[ 2 ].text

		# output
		print( "\t".join( ( speaker, verb, quotation ) ) )

	
# error; unknown input
else : usage()

# done
exit
