#!/usr/bin/env bash

# carrel2model.sh - a front-end to ./bin/corpus2file.sh and ./bin/template2html.sh

# Eric Lease Morgan <emorgan@nd.edu>
# August 11, 2019 - first documentation


# configure
CARRELS='./carrels'
ETC='./html/etc'
CORPUS2FILE='./bin/corpus2file.sh'
TEMPLATE2HTML='./bin/template2html-model.sh'
TXT='txt/*.txt'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <short-name>" >&2
	exit
fi

# get input 
CARREL=$1

# do the work and done
find $CARRELS/$CARREL/$TXT | parallel $CORPUS2FILE {} > "$CARRELS/$CARREL/etc/$CARREL-model.txt"
$TEMPLATE2HTML $CARREL > "$CARRELS/$CARREL/$CARREL-model.html"
exit
