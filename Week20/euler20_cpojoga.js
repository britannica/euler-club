// Using JS build in BigNumbers
const factorial = (n) => {
	const big1 = BigInt(1);
    const bigN = BigInt(n);
    return (bigN <= big1) ? big1 : bigN * factorial(bigN - big1);
}
const sumOfDigits = str => str.split('').reduce((a, b) => parseInt(a) + parseInt(b));

console.log(sumOfDigits(factorial(100).toString()));
// 648