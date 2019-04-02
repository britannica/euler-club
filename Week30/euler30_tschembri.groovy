 /* 
 Euler 30 in Groovy
 Can be tested @: https://www.jdoodle.com/execute-groovy-online
 
 The actual problem is: what is the upper limit of the loop? 
 The max value of a digit ^ 5 is 9 ^ 5.

 The max values are:
 
 1 digit:  1 * 9^5 = 59049
 2 digits: 2 * 9^5 = 118098 
 3 digits: 3 * 9^5 = 177147 
 4 digits: 4 * 9^5 = 236196 
 5 digits: 5 * 9^5 = 295245 
 6 digits: 6 * 9^5 = 354294 
 7 digits: 7 * 9^5 = 413343 

 We will stop at 6 digits because with 7 digits, the max value of sum of each digit ^ 5 has at most 6 digits.
 
 So the upper limit of the loop will be 354294
  
*/
 
 print (((2..<354294).findAll { Integer.toString(it).collect { Math.pow( Integer.parseInt(it), 5 ) }.sum() == it }).sum())
 
/* 

output:
 
 443839
 
*/
