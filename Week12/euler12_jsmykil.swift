import Foundation;

func getTriangularNumber(number:Int)->Int {
    var result = 0
    for i in 1...number {
        result = result + i
    }
    return result
}

func getFactors(number:Int)->[Int] {
    let floatingNumber = Double(number);
    let floatingNumberSquareRoot = sqrt(floatingNumber).rounded()
    let goalNumber = Int(floatingNumberSquareRoot);
    var arrayOfInts: [Int] = []
    for i in 1...goalNumber {
        if (number%i == 0) {
            arrayOfInts.append(i);
        }
    }
    return arrayOfInts
}

let numberOfMinDesiredFactors = 501
var count = 0;
var i = 1;
while count < numberOfMinDesiredFactors {
    let nthFactor = getTriangularNumber(number: i);
    let factors = getFactors(number: nthFactor);
    count = factors.count * 2;
    i = i + 1;
}
print(getTriangularNumber(number: i-1))
