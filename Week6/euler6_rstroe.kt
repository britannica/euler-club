/**
 * How to run this Kotlin code: 
 * 1) copy the code and paste it to https://try.kotlinlang.org/
 * 2) enter 100 on the Program arguments line above the code
 * 3) hit the Run green arrow on the right side of the screen
 */

fun main(args : Array<String>) { 

  if (args.size == 0) {
      println("Please enter an Int argument value")
  } else {

      val range = 1..args[0].toInt()   // catch NumberFormatException... 

      // using sum and map: returns a list containing the results of applying the given transform function to each element in the original collection. 
      println( range.sum()*range.sum() - range.map { it*it }.sum() ) 

      // using sumBy: returns the sum of all values produced by the function applied to each element in the sequence.
      println( range.sum()*range.sum() - range.sumBy { it*it } )    

 }
}
