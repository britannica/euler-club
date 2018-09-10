\ Euler6 in FORTH 
\ Can be tested @ https://tio.run 
\ The sum of the squares of the first n natural numbers is: ( n ( n + 1 )( 2n + 1 ) ) / 6 
\ The square of the sum of the first n natural numbers is:  ( n ( n + 1 ) / 2 ) ^ 2 

: sum_square dup dup 1 + * swap 2 * 1 + * 6 / ;
: square_sum dup dup 1 + * 2 / dup * ;
: euler6 dup square_sum swap sum_square - ;
100 euler6 .

\ output: 25164150 
