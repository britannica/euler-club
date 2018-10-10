fun main(args : Array<String>) {

  println("Sum = ${primeNumbers().takeWhile { it < 2000000 }.toList().sum()}")

}

fun primeNumbers(): Sequence<Long> = generateSequence(2L) { previous ->
  var number = previous + if ((previous % 2) == 0L) 1 else 2
  while (!number.isPrimeNumber()) number += 2
  number
}

fun Long.isPrimeNumber(): Boolean {
  var i = 2L;
  while (i <= Math.sqrt(this.toDouble())) {
    if (this % i == 0L)
        return false;
    i++;
  }
  return true;
}

//soo slow
//fun Int.isPrimeNumber(): Boolean {
//    if (this <= 1) return false
//    for (i in 2 until this)
//        if (this % i == 0)
//            return false
//    return true
//}

//way too slow
fun primeNumbersSlow(): List<Int> {
    val listOfNumbers = (2..2000000).toList()
    return listOfNumbers.fold(listOfNumbers, { acc, value -> acc.filterNot { it != value && it % value == 0 } })

    // fold takes an initial accumulator value and a combining function and builds its return value
    // by consecutively combining current accumulator value with each collection element, replacing the accumulator
    // (applying operation from left to right to current accumulator value and each element)
    // https://kotlinlang.org/docs/reference/lambdas.html
}
