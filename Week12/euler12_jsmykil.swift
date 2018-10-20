// [Done] exited with code=0 in 1.367 seconds
// 🙄 This is annoying but is necessary to do 
// square root
import Foundation;

// Returns the nth 🔺 number
func getTriangularNumber(number:Int)->Int {
    var result = 0
    for i in 1...number {
        result = result + i
    }
    return result
}

// Returns an array of factors up until the ⬜ root
func getFactors(number:Int)->[Int] {
    // Finding of the ⬜ root of our number involves 
    // first turning it into a floaitng point number
    let floatingNumber = Double(number);
    // Get the ⬜ root of our number and use 🎒 rounding
    let floatingNumberSquareRoot = sqrt(floatingNumber).rounded()
    // Convert the double back into an int so we can
    // ➰ to it, otherwise we would have to use stride.
    let goalNumber = Int(floatingNumberSquareRoot);
    // Storage for all of our factors
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
    // Count the number of factors and double it.
    // Are all triangle numbers square rootable with a whole number?
    count = factors.count * 2;
    i = i + 1;
}
print(getTriangularNumber(number: i-1))
