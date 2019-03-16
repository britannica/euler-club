let s = 1, n = 1;

for (let i = 1; i < 1001; i++) {
  n += i * 8 - 6;
  s += n * 4 + i * 12;
}

console.log(s); // 5343342001




// Solution: 
// Writing all diagonal numbers for a 4x4 table:

// s =  1       +   (3 + 5 + 7 + 9)       +     (13, 17, 21, 25)       +        (31 + 37 + 43 + 49)     
//                  i=1                         i=2                             i=3              
//                  d=5-3, (2i)                 d=17-13=4 (2i)                  d=6 (2i)
// n=1 (first)      n=3 = (1+8*1-6)             n=13 = (3+8*2-6)                n=31 = [13+d+(d-2)*3] = 4d-6 = 8i-6 
// s=1 (sum)        s=n + n+d + n+2d + n+3d
//                  s1 = 4n + 6d = 4n + 12i