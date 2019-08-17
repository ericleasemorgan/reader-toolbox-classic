#!/usr/bin/env bash

CARREL2SEARCH='./bin/carrel2search.pl'

if [[ -z $1 ]]; then
	echo "Usage $0 <short-name>" >&2
	exit
fi

CARREL=$1

$CARREL2SEARCH $CARREL > "./html/$CARREL-search.html"