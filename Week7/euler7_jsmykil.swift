import Foundation

func isPrime(numberValue:Int, root:Int) -> Int {
    for n in 2...root {
        if (numberValue % n == 0) {
            return n;
        }
    }
    return 0;
}

var start:Int = 3;
var end:Int = 10001;
var numberOfPrimes = 1;
while numberOfPrimes < end {
    let number1 = Double(start);
    let root1 = Int(ceil(number1.squareRoot()));
    let numberInt1 = Int(number1);
    if (isPrime(numberValue:numberInt1, root:root1) == 0 ? true : false) {
        numberOfPrimes += 1;
        if numberOfPrimes == end {
            print(numberInt1);
        }
    }
    start += 1;
}

print(numberOfPrimes);

