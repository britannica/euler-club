const divisibles = [3, 5];
const array = Array.from(Array(999)).map((v, i) => ++i).filter(v => divisibles.some(d => v % d === 0));
const answer = array.reduce((sum, val) => sum + val);

console.log(answer);
