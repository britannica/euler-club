const comb = (t, c) => {
    let s = 0;
    for (let i = 0; i <= t / c[0]; i++) {
        if (t - i * c[0] === 0) {
            s++
        } else if (t - i * c[0] > 0) {
            s += comb(t - i * c[0], c.slice(1))
        }
    }
    return s;
}
  
console.log(comb(200, [200, 100, 50, 20, 10, 5, 2, 1]));
// 73682