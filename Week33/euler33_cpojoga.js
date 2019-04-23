let numProd = 1;
let denProd = 1;

for (let i = 1; i <= 8; i++) {
  for (let j = i + 1; j <= 9; j++) {
    for (let x = j; x <= 9; x++) {
      if ((i * 10 + x) / (j * 10 + x) === i / j ||
          (x * 10 + i) / (x * 10 + j) === i / j ||
          (i * 10 + x) / (x * 10 + j) === i / j || 
          (x * 10 + i) / (j * 10 + x) === i / j ) {
        numProd *= i;
        denProd *= j;
      }
    }
  }
}

// Euclidean Algorithm for Greatest Common Divisor (GCD), Recursive version
function gcd(a, b) {
  if (b == 0) return a;
  return gcd(b, (a % b));
}

console.log(denProd / gcd(denProd, numProd)); 
// 100 (0ms);


/* 
In the for loop I created all combinations 
of i and j, where (1 <= i <= 8) and (i < j <= 9)
and checked if any of this 4 combinations (ix/jx, xi/xj, ix/xj, xi/jx) === i/j:
If yes, I'm keeping only the `numProd *= i`, `denProd *= j`.


Using Euclidean Algorithm for Greatest Common Divisor (GCD)
Assuming you want to calculate the GCD of 316/1240

1240 % 316 = 292
316 % 292 = 24
292 % 24 = 4
24 % 4 = 0   |  GCD = 4

316/1240 can be simplified to 79/310

Returning, `denProd / GCD`
*/
