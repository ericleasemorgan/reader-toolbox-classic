#!/usr/bin/env python

# tsv2dendogram.py - given a TSV file of a particular shape, visualize the file as a dendrogram


# require
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import sys

# sanity check
if len( sys.argv ) != 2 :
	sys.stderr.write( 'Usage: ' + sys.argv[ 0 ] + " <TSV>\n" )
	exit()

# get input
file = sys.argv[ 1 ]

# create a dataframe, and extract the values
df = pd.read_csv( file, sep='\t' )

help( plt.pcolor)
plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns, rotation=90 )
plt.show()