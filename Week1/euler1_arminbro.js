const sumOfMultiples = (sum, max, validateMultiples) => {
  for (let i = 0; i < max; i++) { validateMultiples(i) && (sum += i) }
  return sum;
};

console.log(sumOfMultiples(0, 1000, val => val % 3 === 0 || val % 5 === 0 ));
