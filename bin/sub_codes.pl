#!perl

use strict;
use warnings;
use feature qw/ say /;

# open the tab seperated file given on the command line
open( my $fh,'<',$ARGV[0] ) || die "Can't open file: $!";

my $header = <$fh>;

LINE: while ( chomp( my $line = <$fh> ) ) {

	# get the SKU and name by splitting on a tab character
	my ( $sku ) = split( "\t",$line );

	# assume the SKU is delimited by a '-' character
	my @sku_parts = split( '-',$sku );
	my ( $new_sku,@new_sku );

	# find the number in the SKU and move it to the front
	for ( my $i = 0; $i <= $#sku_parts; $i++ ) {

		if ( $sku_parts[$i] =~ /^\d+$/ ) {
			@new_sku = ( splice( @sku_parts,$i,1 ),@sku_parts );
		}
	}

	if ( ! @new_sku ) {
		# we failed to find the number
		warn "Didn't know how to handle: $sku";
		$new_sku = $sku;
	} else {
		$new_sku = join( '-',@new_sku );
	}

	$line =~ s/$sku/$new_sku/g;
	say $line;
}

close( $fh );
