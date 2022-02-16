#!/usr/bin/env python

# compute-stopwords.py - given a directory of *.txt files, output a computed list of stop words

# September 2, 2020 - first cut


# configure
DIRECTORY = './library/wisdom/txt/*.txt'
TRESHOLD  = 0.001

# require
import glob
import numpy as np
import pandas as pd
import string
import sys
import math

# initialize
files = []
words = ''

# feature normalization process
def normalize( words ) :

	# initialize
	table = str.maketrans( '', '', string.punctuation )

	# lowercase, split, remove punctuation and done
	words = words.lower().split()
	words = [ word.translate( table ) for word in words ]
	return words

# process each txt file in the directory
for file in glob.glob( DIRECTORY ):
	
	# read the file
	data = open( file ).read()

	# update
	words = words + data
	files.append( file )

# get a list of all the words in the corpus
words = sorted( frozenset( normalize( words ) ) )
files = sorted( files )

# create a zero-filled data frame; initialize a term-document matrix
zeros = np.zeros( shape=( len( files ), len( words ) ) )
df   = pd.DataFrame( zeros, index=files, columns=words )

# process each file, again; populate the matrix
for file in files :

	# read the file; get all the words
	sys.stderr.write( file + "\n" )
	words = normalize( open( file ).read() )

	# process each word and update the matrix accordingly
	for word in frozenset( words ) : df.at[ file, word ] = words.count( word )

# compute entropy for each word in each file
entropies = {}
for file in files :

	# get the total number of words in the given file
	total = df.loc[ file ].sum()
	
	words = frozenset( normalize( open( file ).read() ) )

	# process each word in the dictionary
	for word in words :

		# initialize
		count = df.at[ file, word ]
		if count < 1 : continue
		
		# compute
		p = count/total
		l = math.log( p )
		e = ( p * l ) * -1
		
		# initialize or update the entropy value of each word
		if word not in entropies : entropies[ word ] =  e
		else                     : entropies[ word ] += e

# compute stop words
stopwords = {}
D         = len( files )
for word in list( df.columns ) :

	count          = df[ word ].sum() 
	approximation  = ( 1 - math.exp( ( count * -1 ) / D ) )
	score          = approximation - entropies[ word ]
	if score < TRESHOLD : stopwords[ word ] = score

# sort, output, and done
stopwords = sorted( stopwords.items(), key=lambda x: x[ 1 ], reverse=False )
for stopword in stopwords : print( str( stopword[ 0 ] ) )
exit()



