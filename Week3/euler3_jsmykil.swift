func isPrime(number: Double) -> Bool {
	for x in stride(from: 2, through: number-1, by: 1) {
		if (number.truncatingRemainder(dividingBy: x) == 0) {
			return false
		}
	}
	return true;
}

var primes: Double = 0;
let goal : Double = 600_851_475_143.0;
var root : Double = goal.squareRoot()
	root.round()

for x in stride(from: root, through: 2, by: -1) {
	let onesPlace = x.truncatingRemainder(dividingBy: 10);
	if (onesPlace == 1 || onesPlace == 3 || onesPlace == 7 || onesPlace == 9){
		let tmp = goal.truncatingRemainder(dividingBy: x);
		if (tmp == 0 && isPrime(number: x)) {
			primes = x;
			break;
		}
	}
}

print(primes);
