#!/usr/bin/env bash

# carrel2model.sh - a front-end to ./bin/corpus2file.sh and ./bin/template2html.sh

# Eric Lease Morgan <emorgan@nd.edu>
# August 11, 2019 - first documentation


# configure
CARRELS='./etc/carrels'
ETC='./html/etc'
CORPUS2FILE='./bin/corpus2file.sh'
HTML='./html'
TEMPLATE2HTML='./bin/template2html-model.sh'
TXT='txt'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <short-name>" >&2
	exit
fi

# get input 
CARREL=$1

# do the work and done
find "$CARRELS/$CARREL/$TXT" -name "*.txt" | parallel $CORPUS2FILE {} > "$ETC/$CARREL-model.txt"
$TEMPLATE2HTML $CARREL > "$HTML/$CARREL-model.html"
exit
