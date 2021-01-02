#!/usr/bin/env bash

# vec2model.sh - create a topic model from a previously created set of MALLET vectors

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 4, 2020 - copied to Reader Toolbox


# configure
MALLETHOME='./mallet'
MODELDIR='tmp/mallet'
VECTORS='model.vec'
MODEL2REPORT='./bin/model2report.py'

# sanity check
if [[ -z $1 || -z $2 || -z $3 ]]; then
	echo "Usage: $0 <number of topics> <number of dimensions> <number of documents>" >&2
	exit
fi

# get input
TOPICS=$1
DIMENSIONS=$2
TOPDOCS=$3

# initialize
PWD=`pwd`
MODEL="$PWD/$MODELDIR"

# do the work
$MALLETHOME/bin/mallet train-topics \
	--input $MODEL/$VECTORS \
	--num-topics $TOPICS \
	--num-top-words $DIMENSIONS \
	--num-top-docs $TOPDOCS \
	--num-iterations 1200 \
	--num-threads 10 \
	--optimize-interval 10 \
	--output-doc-topics $MODEL/topics.tsv \
	--output-topic-docs $MODEL/documents.txt \
	--output-topic-keys $MODEL/keys.tsv \
	--random-seed 42 \
	--topic-word-weights-file $MODEL/weights.tsv \
	--word-topic-counts-file $MODEL/counts.txt \
	--xml-topic-phrase-report $MODEL/phrases.xml \
	--xml-topic-report $MODEL/topics.xml

# report and done
$MODEL2REPORT
exit
