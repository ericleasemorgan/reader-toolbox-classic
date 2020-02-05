#!/usr/bin/env python

# word2hypernym.py - given a study carrel, output a frequencies list of broader (key)words

# configure
DB = 'etc/reader.db' 
SQL = 'SELECT keyword FROM wrd GROUP BY keyword ORDER BY COUNT( keyword ) DESC;'
#SQL = "select lemma from pos where pos like 'J%' group by lemma order by count(lemma) desc;"
#SQL = "select lemma from pos group by lemma order by count(lemma) desc;"

# require
from nltk.corpus import wordnet as wn
import sqlite3
import sys

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <carrel>\n" )
	exit()

# get input
carrel = sys.argv[ 1 ]

# initialize
database    = carrel + '/' + DB
frequencies = {} 

# connect to the study carrel and process search result
cursor = sqlite3.connect( database ).cursor()
for record in cursor.execute( SQL ):
	
	# parse
	keyword = record[ 0 ]
	
	# try to do the work
	try :
		
		# get only the first broader term
		hypernym = wn.synsets( keyword )[ 0 ].hypernyms()[ 0 ].name().split( '.' )[ 0 ]
		
		# update the frequency list
		if ( hypernym in frequencies ) : frequencies[ hypernym ] += 1
		else : frequencies[ hypernym ] = 1
	
	# bogus because I'm not pythonic
	except : foo = 'bar'
		
# process each frequency
for key, value in sorted( frequencies.items(), key=lambda item : item[ 1 ], reverse=True ) : 
	
	# output
	print( "\t".join( [ str( value ), key ] ) )

# done
exit
