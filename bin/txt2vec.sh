#!/usr/bin/env bash

# txt2vec.sh - given a study carrel, create a set of vectors for MALLET	

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 4, 2020 - first cut for the Reader Toolbox


# configure
MALLETHOME='./mallet'
MODELDIR='tmp/mallet'
LIBRARY='library'
VECTORS='model.vec'
CORPUS='txt'
STOPWORDS='etc/stopwords.txt'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <carrel>" >&2
	exit
fi

# get input
CARREL=$1

# initialize
PWD=`pwd`
CORPUS="$PWD/$LIBRARY/$CARREL/$CORPUS"
VECTORS="$PWD/$MODELDIR/$VECTORS"
STOPWORDS="$PWD/$LIBRARY/$CARREL/$STOPWORDS"

# make sane
mkdir -p $MODELDIR

# do the work
$MALLETHOME/bin/mallet import-dir \
	--input $CORPUS \
	--output $VECTORS \
	--keep-sequence TRUE \
    --stoplist-file	$STOPWORDS
    
# done
exit
