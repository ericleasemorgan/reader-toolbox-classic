#!/usr/bin/perl

# measure-lexicon.pl - given a directory of text files and a lexicon, output tfidf scores

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# December 8, 2018 - first cut
# August   3, 2020 - moved to Reader Toolbox


# define
use constant STOPWORDS => 'etc/stopwords.txt';
use constant TXT       => 'txt';
use constant LIBRARY   => './library';

# use/require
use strict;
require './etc/tfidf-toolbox.pl';

# get the input
my $carrel  = $ARGV[ 0 ];
my $lexicon = $ARGV[ 1 ];
if ( ! $carrel or ! $lexicon ) { die "Usage: $0 <carrel> <lexicon>\n" }

# initialize
my $library   = LIBRARY;
my $stopwords = STOPWORDS;
my $txt       = TXT;
$stopwords    = "$library/$carrel/$stopwords";
my %index     = ();
my @corpus    = &corpus( "$library/$carrel/$txt");
my $lexicon   = &slurp_words( $lexicon );

# index the corpus
foreach my $file ( @corpus ) { $index{ $file } = &index( $file, &slurp_words( STOPWORDS ) ) }

# measure tfidf for each item in the lexicon
my $measurements = &measure( \%index, [ @corpus ], $lexicon );

# output a header for a tsv file
my @columns = ( 'file' );
foreach ( sort( keys( %$lexicon ) ) ) { push( @columns, $_ ) }
print join( "\t", @columns ), "\n";

# process each file
foreach my $file ( keys( %$measurements ) ) {

	# re-initialize the record's value
	my @fields = ( $file );
	
	# get the words/scores from the measurement, and process each one
	my $ideas = $$measurements{ $file };
	foreach my $idea ( sort( keys( %$ideas ) ) ) {
		
		# build the record
		push( @fields, $$ideas{ $idea } );
	
	}
	
	# output
	print join( "\t", @fields ), "\n";
	
}
	
# done, even more fun with tfidf
exit;


