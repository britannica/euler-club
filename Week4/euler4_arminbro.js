function getLargestPalindrome(num) {
  let largestPalindrome = 11;

  for (let i = num; i > 11; i--) {
    for (let j = num; j > 11; j--) {
      let val = i * j;
      let revVal = parseInt(val.toString().split('').reverse().join(''), 10);
      if (val === revVal && val > largestPalindrome) largestPalindrome = val;
    }
  }

  return largestPalindrome;
}

console.time('getLargestPalindrome run time');
console.log(getLargestPalindrome(999));
console.timeEnd('getLargestPalindrome run time');
