function getLargestPrimeFactor(number) {
  let divisor = 2;

  while (number > 1) {
    number % divisor === 0 ? number /= divisor : divisor > 2 ? (divisor += 2) : divisor++;
  }

  return divisor;
}
  
console.log(getLargestPrimeFactor(600851475143));
