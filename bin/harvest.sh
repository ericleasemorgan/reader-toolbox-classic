#!/usr/bin/env bash

# harvest.sh - given the short name of a study carrel, cache it locally

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 2, 2020 - first documentation


# configure
LIBRARY='./library'
TMP='./tmp'
URL='http://carrels.distantreader.org/library'
ZIP='study-carrel.zip'

# sanity check
if [[ -z $1 ]]; then
	echo "Usage: $0 <short-name>" >&2
	exit
fi

# initialize
CARREL=$1

mkdir -p $TMP
wget -O $TMP/$CARREL.zip $URL/$CARREL/$ZIP
rm -rf $LIBRARY/$CARREL
mkdir -p $LIBRARY/$CARREL
ROOT=$( unzip -Z ./tmp/$CARREL.zip | sed -n 3p | tr -s ' ' | cut -d ' ' -f9 )
unzip -u $TMP/$CARREL.zip -d $TMP
cp -R  $TMP/$ROOT $LIBRARY/$CARREL
rm -rf $TMP/$ROOT
exit
