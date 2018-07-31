let sum = 0;

for (let i = 0; i < 1000; i++) {
  sum = (i % 3 === 0 || i % 5 === 0) ? sum + i : sum;
}

console.log(sum);
