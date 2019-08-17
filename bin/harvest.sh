#!/usr/bin/env bash

# harvest.sh - given the short name of a study carrel, cache it locally


CARRELS='./etc/carrels'
TMP='./tmp'
URL='http://carrels.distantreader.org/library'
ZIP='study-carrel.zip'

if [[ -z $1 ]]; then
	echo "Usage: $0 <short-name>" >&2
	exit
fi

CARREL=$1

wget -O $TMP/$CARREL.zip $URL/$CARREL/$ZIP
rm -rf $CARRELS/$CARREL
mkdir -p $CARRELS/$CARREL
ROOT=$( unzip -Z ./tmp/$CARREL.zip | sed -n 3p | tr -s ' ' | cut -d ' ' -f9 )
unzip -u $TMP/$CARREL.zip -d $TMP
cp -R  $TMP/$ROOT $CARRELS/$CARREL
rm -rf $TMP/$ROOT
