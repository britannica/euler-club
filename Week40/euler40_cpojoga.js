let fr = '';
let i = 1;
while (fr.length < 1e6 ) fr += i++;

let prod = 1;
for (let j = 0; j <= 6; j++) prod *= fr.charAt( 10 ** j - 1);

console.log(prod);
