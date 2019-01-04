const startY = 1901;
const endY = 2000;

// ===============================================================
// Solution 1 (Brute force) 
// ===============================================================

let sum = 0;
for (let y = startY; y <= endY; y++) 
	for (let m = 0; m < 12; m++) 
  	if ( new Date(y, m, 1).getDay() === 0) sum++;	

console.log(sum);
// Outputs: 171. Performance  1816 ms, http://jsben.ch/ (1200 iterations)



// ===============================================================
//  Solution 2   
// ===============================================================

const nL = {};
const L = {};
const monthDays = [31, 28 ,31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const isLeap = y => !(y % 4) && y % 100 || !(y % 400);

// Generates 2 Objects for all 14 possible combinations: 
for (let i = 0; i < 7; i++) {
  let day = i;
  let dayL = i;
  
  for (let j = 0; j < 12; j++) {
  	if (day % 7 === 0) nL[i] = !nL[i] ? 1 : nL[i] + 1;
    if (dayL % 7 === 0) L[i] = !L[i] ? 1 : L[i] + 1;
    
    day += j === 1 ? 28 : monthDays[j];
    dayL += j === 1 ? 29 : monthDays[j];
  }
}

// Result objects for both leap and non-leap versions 
// (where the index is the first day of the year, value is the number of the matches per year)
// nL = {0: 2, 1: 2, 2: 2, 3: 1, 4: 3, 5: 1, 6: 1}; // Non leap year
// L = {0: 3, 1: 2, 2: 1, 3: 2, 4: 2, 5: 1, 6: 1};  // Leap year

let sum1 = 0;
let firstDay = new Date(startY, 0, 1).getDay();

for (let y = 1901; y <= 2000; y++) {
	sum1 += isLeapY(y) ? L[firstDay % 7] : nL[firstDay % 7]
    firstDay += isLeapY(y) ? 2 : 1; 
}

console.log(sum1);
// Outputs: 171, Performance 805ms, http://jsben.ch/ (184 iterations)
