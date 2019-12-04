#!/usr/bin/env python

# tsv2pca-heat.py - given a TSV file of a particular shape and an integer, plot a heat map of principle components

 
# require
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import sys

# sanity check
if len( sys.argv ) != 3 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <file> <integer>\n" )
	exit()

# get input
file       = sys.argv[ 1 ]
components = int( sys.argv[ 2 ] )

# create a dataframe
df = pd.read_csv( file, sep='\t' )

# remove first column, extract labels and values
df     = df.drop( ['file'], axis=1 )
labels = list( df )
X      = df.values

# initialize a scalar and scale
scalar = StandardScaler()
X      = scalar.fit_transform( X )

# initialize PCA and do the work
pca = PCA( n_components = components )
X   = pca.fit_transform( X )

# plot, output, and done
plt.matshow( pca.components_ )
plt.xticks( range( len( labels ) ), labels, rotation=60 )
plt.colorbar()
plt.show()
