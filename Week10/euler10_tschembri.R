# Euler10 in R
# can be tested @ https://www.tutorialspoint.com/execute_r_online.php

Reduce( '+',                                            # <- sum result

  ( function( num ){                                    # anonymous function
      sieve <- rep( TRUE, num )                         # fill the list with TRUE
      sieve [1] <- FALSE                                # 0 is not a prime number
      for( i in 2:sqrt( num ) ){                        # loop from 2 -> square root of 2000000
        if ( sieve[ i ] ) {                             # if number is prime
          sieve [ seq.int( 2 * i, num, i ) ] <- FALSE   # then all its multiples are not prime numbers 
        }
      }
      return( as.numeric( which( sieve ) ) )            # filter the list and keeps only indexes of TRUE value \
  })(2000000)                                           # and convert them to numeric (53bit) because of integer overflow

)
