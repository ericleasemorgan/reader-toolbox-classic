#!/usr/bin/env perl

# classify.pl - list most significant words in a text; based on http://en.wikipedia.org/wiki/Tfidf

# Eric Lease Morgan <eric_morgan@infomotions.com>
# April 10, 2009 - first investigations; based on search.pl
# April 12, 2009 - added dynamic corpus
# August 3, 2020 - migrated for use with study carrels; easier to use but less flexible


# define
use constant LOWERBOUNDS  => .005;
use constant LIBRARY      => './library';
use constant TXT          => 'txt';
use constant STOPWORDS    => 'etc/stopwords.txt';

# use/require
use strict;
require './etc/tfidf-toolbox.pl';

my $carrel      = $ARGV[ 0 ];
my $lowerbounds = $ARGV[ 1 ];
if ( ! $carrel || ! $lowerbounds ) { die "Usage $0 <carrel> <a threshold value between 0 and 1>\n" }

# initialize
my $library   = LIBRARY;
my $directory = LIBRARY . '/' . $carrel . '/' . TXT;
my @corpus    = &corpus( $directory );

# get stopwords
my $stopwords = "$library/$carrel/" . STOPWORDS;
my %stopwords = ();
open F, "< $stopwords" or die "Can't open $stopwords ($!)\n";
while ( <F> ) { chop; $stopwords{ $_ }++ }
close F;


# index, sans stopwords
my %index = ();
foreach my $file ( @corpus ) { $index{ $file } = &index( $file, \%stopwords ) }

# classify (tag) each document
my %terms = ();
foreach my $file ( @corpus ) {

	my $tags = &classify( \%index, $file, [ @corpus ] );
	my $found = 0;
	my $directory = $directory;
	
	# list tags greater than a given score
	foreach my $tag ( sort { $$tags{ $b } <=> $$tags{ $a } } keys %$tags ) {
	
		if ( $$tags{ $tag } > $lowerbounds ) {
		
			$file =~ s/$directory\///e;
			print "$tag (" . $$tags{ $tag } . ") $file\n";
			
			$terms{ $tag }++;
			$found = 1;
			
		}
		
		else { last }
	
	}
	
	print "\n";
			
}

foreach ( sort { $terms{ $b } <=> $terms{ $a } } keys %terms ) {

	my $key   = $_;
	my $value = $terms{ $key };
	print "$key\t$value\n";

}


# done; more fun!
exit;


