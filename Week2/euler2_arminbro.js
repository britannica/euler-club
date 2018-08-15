function fibSum(n, i = 2, results = [0, 1]) {
  let sum = 0;
  let currentFib = 0;

  while ((currentFib = results[i - 1] + results[i - 2]) <= n) {
    results.push(currentFib);
    (currentFib % 2 === 0) && (sum += currentFib);
    i++;
  }

  return sum;
}

console.log(fibSum(4000000));
