10 REM Euler25 in GW-BASIC
20 REM Download GW-BASIC @ http://robhagemans.github.io/pcbasic/
30 REM 1) Binet's Formula: Fib(n) = round( (Phi ^ n) / sqrt(5) ) [ Phi is the Golden Ratio ]
40 REM 2) The number of digits in any integer x is INT( LOG ( x ) ) + 1
50 REM 3) LOG( ( Phi ^ x ) / sqrt(5) ) = ( x LOG( Phi ) ) - ( LOG ( 5 ) / 2 )
60 REM The answer is: ( x LOG( Phi ) ) - ( LOG ( 5 ) / 2 ) > 999 LOG( 10 )

100 ? cint ( ( ( log(10) * 999 ) + ( log(5) / 2 ) ) / log( 1.6180 ) )

--- screenshot:

run
 4782
Ok
 
