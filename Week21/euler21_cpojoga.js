const arr = [];

function d(n) {
  let sum = 1;
  for (let i = 2; i <= n/2; i++) sum += (n % i) ? 0 : i
  return sum;
}

for (let a = 2; a <= 10000; a++ ) {
	let b = d(a);
	if (d(b) === a && a != b && arr.indexOf(a) === -1 ) arr.push(a, b)
}

console.log(arr.reduce((a, b) => a + b));
// 31626