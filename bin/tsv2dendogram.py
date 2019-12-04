#!/usr/bin/env python

# tsv2dendogram.py - given a TSV file of a particular shape, visualize the file as a dendrogram


# require
from scipy.cluster.hierarchy import dendrogram, ward
import matplotlib.pyplot as plt
import pandas as pd
import sys

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <TSV>\n" )
	exit()

# get input
file = sys.argv[ 1 ]

# create a dataframe, and extract the values
df = pd.read_csv( file, sep='\t' )
X  = df.drop( ['file'], axis=1 ).values

# do the work, output, and done
dendrogram( ward( X ) )
plt.show()
exit()
