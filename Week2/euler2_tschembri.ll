; on any fibonacci sequence, the 3rd one is even
; the formula to find the next even number from the current even number (f(x)) is:
; fib( x + 3 ) = ( fib( x ) * 3 ) + ( fib( x - 1 ) * 2 )
; example: 34  = ( 8 * 3 ) + ( 5 * 2 )
;          144 = ( 34 * 3 ) + ( 21 * 2 )
; can be tested with online LISP interpreter: http://rextester.com/l/common_lisp_online_compiler

( let ( ( sum 0 ) ( x-1 1 ) ( x 2 ) ( x+3 2 ) ) 
  ( loop while ( < x+3 4000000 )
    do (
        setf  sum ( + sum x+3 ) 
              x+3 ( + ( * x 3 ) ( * x-1 2 ) )
              x-1 ( + ( * x 2 ) x-1 ) 
              x x+3
         )
    )
 
    ( print sum ) 
) 
