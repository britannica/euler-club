*-----------------------------------------------------------
* Euler 36 in 68000 assembler
* Can be tested with Easy68K (windows only):
* http://www.easy68k.com/
* trap #15 calls are easy68K specific
*-----------------------------------------------------------

        ORG    $1000

START:                  
 
; ------------
; Main program
; ------------


        move.l  #1000000,d6 ; counter
        clr.l   d7          ; sum = 0
                                
find_pal:

        move.l  d6,d0       ; d0 = d6
        bsr     bin_pal     ; test if binary palindrome
        bne.s   not_pal     ; no -> loop              
                        
        move.l  d6,d1       ; d1 = d6
        bsr.s   digit_pal   ; test if binary number
        bne.s   not_pal     ; no -> loop     
        
        move.l  d6,d1       
        bsr     disp_binary ; display binary palindrome       
        lea     space,a1     
        bsr     disp_string ; display " - "
        bsr     disp_number ; display number      
    
        add.l   d6,d7       ; add number to sum    
    
not_pal: 
        subq.l  #1,d6       ; loop - 1
        bne     find_pal    ; if > 0 then loop
        
        lea     result,a1   ; display result
        bsr     disp_string
        move.l  d7,d1
        bsr     disp_number        
        
        move.w  #9,d0
        trap    #15         ; end


; ------------------------------
; Decimal palindrome
; Input:  D1: number
; Output: CC: true if palindrome
; ------------------------------

digit_pal:

        lea     buf,a0      ; a0 = buffer ("array")

bcl:                        ; here we convert a binary value to an "array" of bytes
        clr.l   d2          ; d2 = 0  (upper 32bit 0)  
        move.l  #10,d0      ; d0 = 10 (divisor)
        bsr     divu64      ; divide the number by 10 
        move.b  d3,(a0)+    ; save remainder in buffer
        tst.l   d1          ; is d1 != 0? 
        bne.s   bcl         ; yes,  there's still some digits
        lea     buf,a1      ; a1 = buffer
        move.w  #0,d0       ; d0 = 0 ( flag, will be 1 if palindrome )
pl:
        cmp.l   a0,a1       ; compare a0 (end of the array) to a1 (beginning)
        bgt.s   p2          ; if a1 > a0, stop
        move.b  -(a0),d1    ; d1 = value pointed by a0 (and decrements a0)
        cmp.b   (a1)+,d1    ; compare d1 with what is pointed by a1 (and inc a1)
        beq.s   pl          ; if they are the same, continue
        move.w  #1,d0       ; if not, set the flag to 1
p2:       
        tst.w   d0          ; test the flag
        rts                 ; return
                
; ------------------------------
; Binary palindrome
; Input:  D0: number
; Output: CC: true if palindrome
; ------------------------------  


bin_pal:    
        move.l  d0,d3       ; save d3       
        move.l  #1,d1       ; d1 = 1
        move.w  #31,d2      ; d2 = 32 ( 32 bits )
loop:
        lsr.l   #1,d0       ; shift d0 <- the removed bit goes to X 
        addx.l  d1,d1       ; shift d1 -> and add X
        dbf     d2,loop     ; do that 32 times
loop2:                      ; now we will remove all the trailing 0
        btst.l  #0,d1       ; test bit 0 of d1
        bne.s   e2          ; if 1, go to e2  
        lsr.l   #1,d1       ; shift d1 ->
        bra.s   loop2       ; loop until a 1 is found    
e2:                         ; here d1 is the binary palindrome of d0
        sub.l   d3,d1       ; substract d1 to d3 (saved d0), if result is 0, they are palindromes
        rts                 ; return

 
; --------------
; Display stuff
; --------------

; binary (in D1)

disp_binary:
       
        move.l  d6,d1       
        move.w  #2,d2 
        move.w  #15,d0  
        trap    #15
        rts


; decimal (in D1)

disp_number:

        move.w  #10,d2      ; base 10
        move.w  #15,d0
        trap    #15
        lea     crlf,a1
        move.w  #13,d0
        trap    #15
        rts

; string (in A1)

disp_string:
        move.w  #14,d0
        trap    #15
        rts 
 
 
; ------------------------------- 
; 64bit division
; comes from Atari ST math lib
; Input:  D0:    divisor
;         D1-D2: number to divide
; Output: D1-D2: divided number
;         D3:    remainder
; -------------------------------   
    
divu64
            move.l  d7,-(sp)
            clr.l   d3

            move.l  #64-1,d7
.loop
            add.l   d1,d1
            addx.l  d2,d2
            addx.l  d3,d3
            bcs     .l1

            cmp.l   d0,d3
            bcs     .l2
.l1
            sub.l   d0,d3
            addq.l  #1,d1
.l2
            dbra    d7,.loop

            move.l  (sp)+,d7
            rts   

            SIMHALT             ; halt simulator

* Put variables and constants here

result:     dc.b    $d,$a,'result = ',0
crlf:       dc.b    ' ',0
space:      dc.b    ' - ',0 

buf: 
            ds.b    100    

    END    START        ; last line of source


-------- 
output

10001110111101110001 - 585585
10010000000001001 - 73737
1101001001001011 - 53835
1100111111110011 - 53235
1001110000111001 - 39993
111110111011111 - 32223
111011111110111 - 15351
10001100110001 - 9009
1110100010111 - 7447
1011001101 - 717
1001001001 - 585
100111001 - 313
1100011 - 99
100001 - 33
1001 - 9
111 - 7
101 - 5
11 - 3
1 - 1

result = 872187

