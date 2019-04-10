/*

Euler 31 in verilog. (well, kind of ;-)) 
Test @ https://www.tutorialspoint.com/compile_verilog_online.php

*/

module main;
    
    integer total = 0;
    integer i,j,k,l,m,n,o;
       
    initial 
    begin
   
        for ( i = 200; i >= 0; i -= 200 ) 
        begin
            for ( j = i; j >= 0; j -= 100 )
            begin
                for ( k = j; k >= 0; k -= 50 )
                begin
                    for ( l = k; l >= 0; l -= 20 )
                    begin
                        for ( m = l; m >= 0; m -= 10 ) 
                        begin
                            for ( n = m; n >= 0; n -= 5 ) 
                            begin
                                for ( o = n; o >= 0; o -= 2 )
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
