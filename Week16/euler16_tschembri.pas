(* Euler16 in P-System PASCAL UCSD                                                                 *)
(* To run it:                                                                                      *)
(* 1) Download the Altair8080 emulator @https://schorn.ch/altair_2.php                             *)
(* 2) Download the UCSD p-system @https://schorn.ch/cpm/zip/ucsd.zip                               *)
(* 3) Unzip the disk images in the same folder                                                     *)
(* 4) start the emulator (altairz80.exe) in a console window                                       *)
(* 5) the pascal editor requires a VT100 terminal, we will need to use a terminal emulator:        *)
(* 6) type: "attach sio 23" : it creates a virtual serial port on the telnet port 23               *)
(* 7) start a terminal emulator (putty for exemple) and start a telnet connection on 127.0.0.1 23  *)
(* 8) type ^E in the emulator window, then "do ucsd"                                               *)
(* 9) From here, use the terminal emulator (see "screenshots" after the program)                   *)


PROGRAM euler16(output);

CONST max = 9;
VAR i, carry, j, prod, sum: Integer;
    digits: Array[0..max] of Integer;

BEGIN
    FOR i:=0 to max DO
    BEGIN
        digits[i]:=0;
    END;

    digits[0] := 1;
    FOR i:=0 TO max DO
    BEGIN
        carry:=0;
        FOR j:=0 TO max DO
        BEGIN
            prod:=digits[j]*2+carry;
            IF prod > 9 THEN
            BEGIN
                carry:=1;
                prod:=prod MOD 10;
            END
            ELSE
                carry:=0;
            digits[j]:=prod;
        END;
    END;
    sum:=0;
    FOR i:=0 TO max DO 
    BEGIN
       sum:=sum+digits[i];
    END;
    WRITE( sum );
END.


------ Screenshots ------

Connected to the Altair 8800 (Z80) simulator Serial Input Output SIO device, line 0


64K CP/M Version 2.2 (SIMH ALTAIR 8800, BIOS V1.28 for UCSD, 09-Apr-07)


LOADING...

Welcome  DSK0,  to

U.C.S.D.  Pascal  System  II.0

Current date is  14-Apr-7

Command: E(dit, R(un, F(ile, C(omp, L(ink, X(ecute, A(ssem, D(ebug,? [II.0]

E

>Edit:
No workfile is present. File? ( <ret> for no file <esc-ret> to exit )
:

<return>
<Here, I type the program then leave the editor (^Z,Q,U)>

Writing..
Your file is 517 bytes long.

Command: E(dit, R(un, F(ile, C(omp, L(ink, X(ecute, A(ssem, D(ebug,? [II.0]

C

PASCAL Compiler [II.0.A.1]
<   0>........
EULER16  [ 4779 words]
<   8>............................
36 lines
Smallest available space = 4779 words

Command: E(dit, R(un, F(ile, C(omp, L(ink, X(ecute, A(ssem, D(ebug,? [II.0]

R

Running...
1366

