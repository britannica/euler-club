/* 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
Answer: 142913828922

📢 Shout out to Eratosthenes and his Sieve 
🏃‍ Run time arounr 2.85 seconds.
*/

// 🤷 necessary for at least square root function
import Foundation 

// Start with the first prime number
var start: Double = 2.0 
// How many prime numbers we want
var end: Double = 2_000_000 
// The square root of the goal number
var squareEnd: Double = end.squareRoot() 
// 🏫 Elementary School rounding of the square root of the goal number
var squareRoundEnd: Double = squareEnd.rounded() 

/*
A poor mans bit array
Create an array with our goal number of items all set to 1 || true which means prime.
This is a super handy little function, don't know if it's any more performant than 
looping, but it seems like it.
*/
var digitsCount = Array(repeating: 1, count: Int(end)) 

// You can't loop through doubles so we have to use stride
for i in stride(from: start, through: squareRoundEnd, by: 1) {
    /*
    Count by i just like Eratosthenes taught us otherwise we are
    in for a long night of code running.
    */
    for x in stride(from: i*2, through: end, by: i) {
        // Can't use modulus with Doubles so we have to use truncatingRemainder
        let tmp = x.truncatingRemainder(dividingBy: i)
        /* 
        If the truncatingRemainder is 0 than the number is
        composite. (That's a fancy pants 🧐 way of saying 'not' prime)
        */
        if (tmp == 0) {
            digitsCount[Int(x-1)] = 0 // 💡 turning the correct bit in our bit array off
        }
    }
}

/*
Now we have to loop through our bit array 
and sum up all the prime numbers
*/
var sum = 0;
for i in 1...digitsCount.count {
    if (digitsCount[i-1] == 1) {
        sum += i
    }
}

/* 
We count 1 as prime so we need to remove it in the end
it's so lonely.
*/

print(sum-1)
