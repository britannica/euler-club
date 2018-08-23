// Big assumption is that our palindrome will be six digits since 999 * 999..101 is a six digit number
// No strings needed
// Finishes ~.500 seconds

func palindrome(tmp:Int) -> Int {
    if (tmp%11 == 0) { /* A six digit palindrome is always divisible by 11 */
        if (tmp/100_000%10 == tmp%10 ) {
            if (tmp/10_000%10 == tmp/10%10) {
                if (tmp/1_000%10 == tmp/100%10) {
                    return(tmp);
                }
            }
        }
    }
    return 0;
}

var x = 999;
var y = 999;
var palindromeMan = 0; /* Does whatever a palindrome can  */

for i in (101...999).reversed() {
    for x in (101...999).reversed() {
        let tmp = i*x;
        if (tmp > 99_999) {
            let palind = palindrome(tmp:tmp);
            if (palind != 0) {
                if (palindromeMan < tmp) {
                    palindromeMan = tmp;
                }
            }
        }
    }
}
print(palindromeMan);
