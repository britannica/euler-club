function fibSum(n, i = 2, results = [0, 1]) {
  if (n < 2) return n;

  while (results[i - 1] + results[i - 2] <= n) {
    results.push(results[i - 1] + results[i - 2]);
    i++;
  }

  return results.reduce((sum, num) => num % 2 === 0 ? sum += num : sum, 0);
}

console.log(fibSum(4000000));
