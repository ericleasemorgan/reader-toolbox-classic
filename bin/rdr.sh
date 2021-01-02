#!/usr/bin/env bash

# rdr.sh - a Bash wrapper around a set of scripts used to interface with a Distant Reader study carrel

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# December 23, 2020 - first cut; at the cabin


COMMANDS=( concordance classify browse cluster info-carrel list-local-inventory list-remote-inventory keywords-sentences list-ngrams measure-ideas word2vec-build word2vec-use mallet-build mallet-use play-hangman play-wordsearch )

# define usage
function usage {

	echo "Usage: rdr <command> where <command> is one of the following:"
	echo
	for COMMAND in "${COMMANDS[@]}"; do
		echo "  * $COMMAND"
	done
	echo
	echo "For more detail, enter 'rdr help <command>' where <command> is on of the item above"
	exit

}

# sanity check
if [[ -z $1 ]]; then usage; fi

# get input
COMMAND=$1

if [[ $COMMAND == 'commands' ]]; then
	echo "RDR commands include: concordance, classify, browse, cluster, info-carrel, list-local-inventory, list-remote-inventory, keywords-sentences, list-ngrams, measure-ideas, word2vec-build, word2vec-use, mallet-build, mallet-use, play-hangman, play-wordsearch" >&2
	
elif [[ $COMMAND == 'concordance' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/concordance.pl $CARREL "$OPTIONS"

elif [[ $COMMAND == 'classify' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/classify.pl $CARREL $OPTIONS

elif [[ $COMMAND == 'browse' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/browse.sh $CARREL 

elif [[ $COMMAND == 'cluster' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/cluster.py $CARREL $OPTIONS

elif [[ $COMMAND == 'info-carrel' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/info-carrel.sh $CARREL $OPTIONS

elif [[ $COMMAND == 'list-local-inventory' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/list-local-inventory.sh $CARREL $OPTIONS

elif [[ $COMMAND == 'keywords-to-sentences' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/keyword2sentences.pl $CARREL $OPTIONS

elif [[ $COMMAND == 'list-remote-inventory' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/list-remote-inventory.sh $CARREL $OPTIONS

elif [[ $COMMAND == 'list-ngrams' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/ngrams.pl $CARREL $OPTIONS

elif [[ $COMMAND == 'measure-ideas' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/measure-ideas.pl $CARREL $OPTIONS

elif [[ $COMMAND == 'word2vec-build' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/carrel2vec.sh $CARREL $OPTIONS

elif [[ $COMMAND == 'word2vec-use' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/search-vec.py $CARREL $OPTIONS

elif [[ $COMMAND == 'mallet-build' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/txt2vec.sh $CARREL $OPTIONS

elif [[ $COMMAND == 'mallet-use' ]]; then
	CARREL=$2
	OPTIONS=$3
	DOCUMENTS=$4
	$RDR_HOME/bin/vec2model.sh $CARREL $OPTIONS $DOCUMENTS

elif [[ $COMMAND == 'play-hangman' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/hangman.py

elif [[ $COMMAND == 'play-madlib' ]]; then
	CARREL=$2
	OPTIONS=$3
	$RDR_HOME/bin/madlib.py

else usage
fi


