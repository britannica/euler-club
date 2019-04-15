const isPandigitalOf9 = str => str.split('').sort().join('') === '123456789';
const prodIsPandigitalOf9 = (a, b) => isPandigitalOf9('' + a + b + a * b);
const res = [];

for (let i = 1; i < 8; i++) {
    for (let j = 1234; j < 9876; j++) {
        if (i * j > 9876) break; 
        if (prodIsPandigitalOf9(i, j) && res.indexOf(i * j) === -1) res.push(i * j);
    }
}

for (let i = 12; i < 79; i++) {
    for (let j = 123; j < 832; j++) {
        if (i * j > 9876) break;
        if (prodIsPandigitalOf9(i, j) && res.indexOf(i * j) === -1) res.push(i * j);
    }
}

console.log(res.reduce((a, b) => a + b));
// 45228 (41ms)



/*  *** Explanation ***

Minimal pandigital of 9 is: 123456788, 
Maximum is: 987654321

We can get the 9 digit pandigital and unusual product only in this 4 combinations (1d stands for 1 digit number): 
1.  1d x 4d = 4d (Maximum product to get a 4 digit number: 1 x 9876, or 8 x 1234 )
2.  2d x 3d = 4d (Maximum product to get a 4 digit number: 12 x 832 or 79 x 123 )

We will ignore the next iterations because we are looking to get unique products. We already have this products from the first 2 iterations
3.  3d x 2d = 4d
4.  4d x 1d = 4d

*/