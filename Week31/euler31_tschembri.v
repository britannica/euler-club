/* 
Euler 31 in Verilog ( well, kind of ;-))
Test @https://www.tutorialspoint.com/compile_verilog_online.php

Explanation:

The program will loop and find all the combinations of numbers <= 200. 
There's no inner loop with 1p because each combination that is < 200 is "filled up" with 1p.

For example, if we search all the combinations for 10:

m=n=o=10
The "o" loop will iterate 6 times and count these combinations:
1. 1 1 1 1 1 1 1 1 1 1 
2. 2 1 1 1 1 1 1 1 1
3. 2 2 1 1 1 1 1 1
4. 2 2 2 1 1 1 1
5. 2 2 2 2 1 1
6. 2 2 2 2 2

m=10,n=o=5
The "o" loop will iterate 3 times and count these combinations:
1. 5 1 1 1 1 1
2. 5 2 1 1 1
3. 5 2 2 1

m=10,n=o=0
The "o" loop will iterate 1 time and count this combination:
1. 5 5

m=0=n=o=0
The "o" loop will iterate 1 time and count this combination:
1. 10

Total: 11 combinations:
  
*/

module main;
    
    integer total = 0;
    integer i,j,k,l,m,n,o;
       
    initial 
    begin
       
      for ( i = 200; i >= 0; i -= 200) 
      begin
	  for ( j = i; j >= 0; j -= 100)
	  begin
	     for ( k = j; k >= 0; k -= 50)
	     begin
	         for ( l = k; l >= 0; l -= 20)
	         begin
		     for ( m = l; m >= 0; m -= 10) 
		     begin
			 for ( n = m; n >= 0; n -= 5) 
			 begin
			     for ( o = n; o >= 0; o -= 2)
			     begin
				 total++;
		 	     end
			 end
		     end
	         end
	     end
	 end
     end
		    
     $display(total);
     $finish ;
    end
endmodule

/* 

output

$iverilog -o main *.v
$vvp main
      73682

*/
