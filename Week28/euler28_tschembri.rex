/* 

Euler 28 in rexx. Can run online @https://www.tutorialspoint.com/execute_rexx_online.php 

The numbers on the 5x5 diagonal are: 1 3 5 7 9 13 17 21 25
The numbers on the 7x7 diagonal are: 1 3 5 7 9 13 17 21 25 31 37 43 49
The numbers on the 9x9 diagonal are: 1 3 5 7 9 13 17 21 25 31 37 43 49 57 65 73 81

it seems there's a kind of pattern, I don't know if there's some math formula that can confirm it:
the difference between numbers 1 to 5  ( 1 -> 9 ) is 2.
the difference between numbers 5 to 9  ( 9 -> 25 ) is 4.
the difference between numbers 9 to 13 ( 25 -> 49 ) is 6.
the difference between numbers 13 to 17 ( 49 -> 91 ) is 8.
We can assume that the difference between the 4 next numbers will be 10 (again, it is empirical) then 12, 14, ...
With a 5x5 square, there are 2 groups, with a 9x9 group, there are 4 groups, 
we can assume there always will be int(n/2). (well if the size of the square is odd)

*/


size = 1001
result = 1
n = 1

do i = 1 to size / 2 
   do j = 1 to 4
      n = n + ( i * 2 )
      result = result + n
   end 
end

say 'result = ' result

--- output:

$rexx main.rex
result =  669171001
