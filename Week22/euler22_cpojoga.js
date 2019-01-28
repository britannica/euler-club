// Read sync the names.txt 
const fs = require('fs');
const path = require("path");
const fileData = fs.readFileSync(path.resolve(__dirname, "./names.txt"), 'utf-8', (err, data) => { 
    if (err) throw err; 
});

// Striping the double quotes, splitting into words and sorting the resulting array
const arrOfNames = fileData.replace(/\"/g, "").split(',').sort(); 

const score = (name, pos) => {
    // Array with values for each character, where 64 is 'A'.charCodeAt() - 1
    const arr = name.split('').map(ch => ch.charCodeAt() - 64); 
    // Returning the sum of the array values * index:
    return arr.reduce((a, b) => a + b) * pos;
}

const scoreArr = arrOfNames.map((name, i) => score(name, i + 1)); // Array of scores

console.log(scoreArr.reduce((a, b) => a + b));
// 871198282