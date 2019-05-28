// Using Pseudocode from https://en.wikipedia.org/wiki/Primality_test
function isPrime(n) {
    if (n <= 3) 
        return n > 1;
    else if (n % 2 === 0 || n % 3 === 0) 
        return false;

    let i = 5;
    while (i * i <= n) {
        if (n % i === 0 || n % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
} 

function isTruncablePrime(n) {
    if (!isPrime(n)) return false;

    const s = n + '';
    for (let i = 1; i < s.length; i++) {
        if (!isPrime(parseInt(s.slice(i))) || !isPrime(parseInt(s.slice(0, i))))
            return false
    }

    return true
}

const res = [];
let n = 11;
while (res.length <= 10) {
    if (isTruncablePrime(n)) 
        res.push(n);
    
    n += 1;
}

console.log(res.reduce((a, b) => a + b), res);
// [ 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397 ]  =>  748317
// time 94ms