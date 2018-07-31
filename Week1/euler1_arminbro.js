const arrayofMultiples = [];
let sum = 0;

for (let i = 0; i < 1000; i++) {
  (i % 3 === 0 || i % 5 === 0) && arrayofMultiples.push(i);
}

sum = arrayofMultiples.reduce((sum, val) => sum + val, sum);

console.log(sum);
