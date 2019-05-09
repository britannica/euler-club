const p1 = [];
const p2 = [];
for (let i = 0; i < 1000000; i++) {
  const x = i.toString();
  if (x === x.split('').reverse().join('')) {
    const binary = parseInt(x, 10);
    const binary2 = binary.toString(2)
    if (binary2 === binary2.split('').reverse().join('')) {
      p1.push(x);
      p2.push(binary2);
    }
  }
}

console.log(palindromes.reduce( function(a, b){
  return +a + +b;
}));