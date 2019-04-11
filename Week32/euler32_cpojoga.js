const isPandigitalOf9 = str => str.split('').sort().join('') === '123456789';
const isPandigitalOf9Prod = (a, b) => isPandigitalOf9('' + a + b + a * b);
const res = [];

for (let i = 1; i < 9; i++) {
  for (let j = 1234; j < 9876; j++) {
    if (res.indexOf(i * j) === -1 && isPandigitalOf9Prod(i, j)) res.push(i * j)
  }
}
for (let i = 12; i < 98; i++) {
  for (let j = 123; j < 987; j++) {
    if (res.indexOf(i * j) === -1 && isPandigitalOf9Prod(i, j)) res.push(i * j)
  }
}

console.log(res.reduce((a, b) => a + b));
// 45228 (199ms)