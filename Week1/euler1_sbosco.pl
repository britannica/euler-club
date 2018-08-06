#!/usr/local/bin/perl -w

$total = 0;
foreach $x (1..999) {
    if ($x%3 == 0 || $x%5 == 0) {
        $total += $x; 
    }
}
print "$total\n";
