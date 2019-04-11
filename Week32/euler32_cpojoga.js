// Generate all 9 digits pandigitals:
const pandigitals = [];
const comb = (d, u) => {
  for (let i = 0; i < d.length; i++) {
    const u1 = [...u, d[i]];
    
    if (u1.length === 9) 
      pandigitals.push(u1.join(''));
    else
      comb([...d.slice(0, i), ...d.slice(i + 1)], u1);
  }
}

const num = (str, start, end) => parseInt(str.substring(start, end));

comb([1,2,3,4,5,6,7,8,9], []);

const res = [];
// Find all unique products:
for (let i = 0; i < pandigitals.length; i++) {
    const el = pandigitals[i];
    const prod = num(el, 5, 9);

    if (res.indexOf(prod) === -1 && (num(el, 0, 1) * num(el, 1, 5) === prod || num(el, 0, 2) * num(el, 2, 5) === prod)) {
        res.push(prod)
    }
}

console.log(res.reduce((a, b) => a + b))
// 45228 (450ms)
