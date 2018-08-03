1 REM Euler Club Week 1
2 REM Mark Wiechec
3 REM to run goto http://www.quitebasic.com/
4 REM copy and paste into window 
5 REM This Solution uses modulus operator
10 LET S = 0
20 FOR X = 1 TO 999
30 IF (X%3=0 OR X%5=0) THEN LET S = S + X
40 NEXT X
50 PRINT S
