* Euler 37 in COBOL
* Try @ https://www.jdoodle.com/execute-cobol-online
* Remove the comments, because online editors don't let enter the comments in column 0

IDENTIFICATION DIVISION.
PROGRAM-ID. EULER37.

DATA DIVISION.
WORKING-STORAGE SECTION.

01  MAX PIC 9(8) VALUE 100000.
01  PRIME PIC 9 VALUE 0 OCCURS 1000000 TIMES.
01  I PIC 9(8). 
01  J PIC 9(8).
01  K PIC 9(8).
01  L PIC 9(8).
01  N PIC 99.
01  R PIC 9.
01  S PIC 999999.

PROCEDURE DIVISION.
    MAIN SECTION.

* build Eratosthenes sieves

    MOVE 1 TO PRIME(1) 
    MOVE 1 TO I
    
    PERFORM UNTIL I > MAX ** 0.5
        ADD 1 TO I
        PERFORM VARYING J FROM I BY 1 UNTIL PRIME( J ) = 0 AND J <  1000000 
        END-PERFORM
        MOVE J TO I
        COMPUTE J = J ** 2
        PERFORM UNTIL J > MAX
            SET PRIME( J ) TO 1
            SET J UP BY I
        END-PERFORM    
    END-PERFORM    
    
* calls Trunc subprogram until n = 11

    MOVE 0 TO N
    MOVE 0 TO S
    MOVE 8 TO I

    PERFORM UNTIL N >= 11
        PERFORM TRUNC
        IF R = 1 
            ADD 1 TO N
            DISPLAY I
            ADD I TO S
        END-IF
        ADD 1 TO I
    END-PERFORM
    
    
    DISPLAY  S
    
STOP RUN.    
    
* Checks if a number is truncatable    

    TRUNC.
        
* First, from the right: divides the number by 10 until it is = 0
* Exits the subprogram is one of the divisions is not a prime number
* (R is the returned value: 1 if it is truncatable, 0 otherwise)
        
        MOVE I TO K
        PERFORM UNTIL K = 0
            IF PRIME( K ) = 1
                MOVE 0 TO R
                EXIT PARAGRAPH
            END-IF
            DIVIDE K BY 10 GIVING K
        END-PERFORM    
        
* Now, for the left, more complicated, First we find the size
* of the number (could have used round(log10(n)+1) but there are issues
* with rounding the log10 result, I don't have time to investigate
        
        MOVE 0 TO J
        MOVE I TO K
        
        PERFORM UNTIL K = 0 
            ADD 1 TO J
            DIVIDE K BY 10 GIVING K
        END-PERFORM

* Here K is the length of the number
* Value modulo ( 10 ^ length ) is the value without the most significant digit

        PERFORM UNTIL J = 0
            COMPUTE L = 10 ** ( J - 1 )
            COMPUTE K = FUNCTION MOD( I, L ) 
            IF PRIME( K ) = 1
                MOVE 0 TO R
                EXIT PARAGRAPH
            END-IF
            SUBTRACT 1 FROM J
        END-PERFORM

        MOVE 1 TO R
        EXIT PARAGRAPH.

---- Output

00000023
00000037
00000053
00000073
00000313
00000317
00000373
00000797
00003137
00003797
00739397
748317
