* Motorola 68000 assembler
* You can try it on your Commodore Amiga

	MOVE.L	#999,D0		* D0 = Loop index
	CLR.L	D1			* D1 = sum
LOOP:
	MOVE.L	D0,D2		* D2 = D1
	DIVU	#3,D2		* Divide D2 by 3: D2 lower 16 bits = result of int division, upper 16 bits = modulo
	SWAP	D2			* Switch upper 16 bits with lower 16 bits
	TST.W   D2			* Compare lower 16 bits with 0
    BEQ 	SUM			* If zero, means modulo = 0 means multiple of 3, so adds the loop index to the sum
	MOVE.L	D0,D2		* Same thing with 5
	DIVU	#5,D2
	SWAP	D2
	TST.W   D2
	BNE		CONTINUE
SUM	ADD.L	D0,D1
CONTINUE:
	DBF		D0, LOOP	* Loop until D0 >= 0
	
* here the SUM is in D1