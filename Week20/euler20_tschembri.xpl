/* Euler 20 in XPL                                                                    */
/* XPL: 1967 - http://teampli.net/XPL/                                                */ 
/* Download the XPL to C converter at https://sourceforge.net/projects/xpl-compiler/  */
/* (linux or windows + cygwin/WLS required)                                           */

/* 1) Compile the compiler: make                                                      */
/* 2) Add this into the makefile:                                                     */
/*    euler.c: euler20.xpl xpl.h xpl                                                  */
/*    euler: euler20.c libxpl.a                                                       */
/*      	$(CC) euler20.c libxpl.a -o euler20                                   */
/* 3) type: make euler to compile the xpl source and convert it to c and compile it   */
/* 4) type: ./euler20                                                                 */
/* 5) Enjoy the power of XPL                                                          */  


declare a(160) bit(16) initial(1), (i,j,carry,max,n) bit(16);

max = 1;
carry = 0;

do i = 1 to 100;
   do j = 0 to max - 1;
      n = a(j) * i + carry;
      a(j) = n mod 10;
      carry = n / 10;
   end;
   do while carry ~= 0;
       a(max) = carry mod 10;
       carry = carry / 10;
       max = max + 1;
   end;
end;

j = 0;
do i = max-1 to 0 by -1;
  call xprintf('%d',a(i));  /* this external function doesn't exist in the original XPL */
  j = j + a(i);
end; 
output = '';
output = j;

eof

/* screenshot */

ts@tschembri5520:/mnt/c/tmp/xpl/compiler$ make euler
./xpl euler20.xpl -o euler20.c
XPL to C language translator -- version 0.6
29 cards containing 19 statements were compiled.
No errors were detected.
cc euler20.c libxpl.a -o euler20

ts@tschembri5520:/mnt/c/tmp/xpl/compiler$ ./euler20
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
648

ts@tschembri5520:/mnt/c/tmp/xpl/compiler$
