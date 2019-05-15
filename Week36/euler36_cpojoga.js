let sum = 0;

function isB2Palindrome(b10) {
    const b2 = parseInt(b10).toString(2);
    return b2 === b2.split('').reverse().join('');
}

for (let i = 1; i < 1000; i++) {
    const n = i + ('' + i).split('').reverse().join('');
    const n1 = i + ('' + i).split('').reverse().join('').substr(1);
    if (isB2Palindrome(n)) sum += parseInt(n);
    if (isB2Palindrome(n1)) sum += parseInt(n1);
}

console.log(sum);
// 872187  (7.19ms);