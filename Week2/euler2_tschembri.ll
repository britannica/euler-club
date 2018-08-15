; on any fibonacci sequence, the 3rd one is even
; the formula to find the next even number from the current even number (fib( x )) is:
; fib( x + 3 ) = ( fib( x ) * 3 ) + ( fib( x - 1 ) * 2 )
; where fib( x - 1 ) = fib( x - 1 ) + ( fib( x ) * 2 ) 

; Fib numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,...

; example: 34  = ( 8 * 3 ) + ( 5 * 2 )
;          144 = ( 34 * 3 ) + ( 21 * 2 )
;          610 = ( 144 * 3 ) + ( 89 * 2 )
;
; and 5  = ( 2 * 2 ) + 1
;     21 = ( 2 * 8 ) + 5
;     89 = ( 2 * 34 ) + 21

; Insert here [___________________] the name of the famous mathematician who proved that.

; can be tested with online LISP interpreter: http://rextester.com/l/common_lisp_online_compiler

( let ( ( sum 0 ) ( x-1 1 ) ( x 2 ) ( x+3 2 ) ( i 0 ) ) 
  ( loop while ( < x+3 4000000 )
    do (
        setf  sum ( + sum x+3 ) 
              x+3 ( + ( * x 3 ) ( * x-1 2 ) )
              x-1 ( + ( * x 2 ) x-1 ) 
              x x+3
                 
         )
    do ( incf i )
  )
  ( format t "Sum is: ~D - in ~D loops" sum i ) 
) 
