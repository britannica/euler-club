const c = [100, 50, 20, 10, 5, 2, 1];
const t = 200;
let s = 1;

for (let c0 = 0; c0 <= t / c[0]; c0++ ) {
  for (let c1 = 0; c1 <= (t - c0 * c[0]) / c[1]; c1++ ) {
    for (let c2 = 0; c2 <= (t - c0 * c[0] - c1 * c[1]) / c[2]; c2++ ) {
      for (let c3 = 0; c3 <= (t - c0 * c[0] - c1 * c[1] - c2 * c[2]) / c[3]; c3++ ) {
        for (let c4 = 0; c4 <= (t - c0 * c[0] - c1 * c[1] - c2 * c[2] - c3 * c[3]) / c[4]; c4++ ) {
          for (let c5 = 0; c5 <= (t - c0 * c[0] - c1 * c[1] - c2 * c[2] - c3 * c[3] - c4 * c[4]) / c[5]; c5++ ) {
            for (let c6 = 0; c6 <= (t - c0 * c[0] - c1 * c[1] - c2 * c[2] - c3 * c[3] - c4 * c[4] - c5 * c[5]); c6++ ) {
              if ((c0 * c[0] + c1 * c[1] + c2 * c[2] + c3 * c[3] + c4 * c[4] + c5 * c[5] + c6) === t) s++
            }
          }
        }
      }
    }
  }
}

console.log(s);
// 73682