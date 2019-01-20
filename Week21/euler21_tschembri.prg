Euler 21 in dBase III
(dBase III language manual can be dowloaded here: http://iti-copa.weebly.com/uploads/1/7/9/9/1799894/dbase_iii_plus_tutorial.pdf)
We need two files for this program: euler21.prg is the main program and eulsum.prg is a procedure.
dBase III doesn't support procedures in the same file, so we need to put it in an external file.

To run this program:

1) Download dBase III+: https://winworldpc.com/download/4632c3b6-0018-c39a-11c3-a4e284a2c3a5
2) Install it in a MSDOS virtual box (vDos for example) or use it in the command box of a 32bit Windows version
3) put the 2 files in the same directory as dBase
4) run dBase (dbase.exe)
5) leave the assist mode (esc)
6) run the program: DO euler21

* --- save from here in a file named EULER21.PRG -------------

CLEAR                              
SET TALK OFF

sumAmicable = 0
i = 2
max = 10000

? TIME()
DO WHILE i <= max
  
   @ 1,15 SAY i
   sumFactorsI = 0
   DO eulsum WITH i, sumFactorsI
  
   IF sumFactorsI > i .AND. sumFactorsI <= max
      sumSum = 0
      DO eulsum WITH sumFactorsI, sumSum
      IF sumSum = i
         sumAmicable = sumAmicable + sumSum + sumFactorsI 
      ENDIF
   ENDIF
   
   i = i + 1
ENDDO

? ""
? "result = ", sumAmicable
? TIME()

* --- end of EULER21.PRG ---

* --- save from here into a file named EULSUM.PRG ---

PARAMETER number, result
PRIVATE i

* because of some mathematical rule I don't remember, we can stop at sqrt(number)

sqrt_number = INT(SQRT(number))
s = 1

* if the number is a square, we won't use the factor twice

IF number = sqrt_number * sqrt_number
   s = s + sqrt_number 
   sqrt_number = sqrt_number - 1
ENDIF

* iterates to find the factors

i = 2
DO WHILE i <= sqrt_number
   IF MOD (number, i) = 0
      s = s + i + ( number / i )
   ENDIF  
   i = i + 1
ENDDO   

STORE INT(s) TO result
RETURN

* --- end of EULSUM.PRG ---

--- Screenshot:

12:49:53            10000

result =       31626
12:56:29



