function sumOfMultiples(max, divisibles) {
  const array = Array.from(Array(max - 1)).map((v, i) => ++i).filter(v => divisibles.some(d => v % d === 0));
  return array.reduce((sum, val) => sum + val);
}

console.log(sumOfMultiples(1000, [3, 5]));
