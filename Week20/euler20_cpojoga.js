// Using JS build in BigNumbers
const factorial = n => n <= 1n ? 1n : n * factorial(n -1n);
const sumOfDigits = str => str.split('').reduce((a, b) => parseInt(a) + parseInt(b));

console.log(sumOfDigits(factorial(100n).toString()));
// 648