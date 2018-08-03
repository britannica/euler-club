function sumOfMultiples(max, divisbles) {
  const array = Array.from(Array(max - 1)).map((v, i) => ++i).filter(v => divisibles.some(d => v % d === 0));
  const answer = array.reduce((sum, val) => sum + val);

  console.log(answer);
}

sumOfMultiples(1000, [3, 5]);
