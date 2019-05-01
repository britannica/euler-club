/*

Euler 34 in Java

The upper limit is a number where all the digits are 9.
Now, we need to find a number made of 9s where the numbers of digits of the sum of each !9 is > to the number ( hm, not sure I'm clear )
9! = 362,880, doesn't work
9! + 9! = 725,760, doesn't work
9! + 9! + 9! = 1,088,640, doesn't work
9! + 9! + 9! + 9! = 1,451,520, doesn't work
9! + 9! + 9! + 9! + 9! = 1,814,400, doesn't work
9! + 9! + 9! + 9! + 9! + 9! = 2,177,280, doesn't work
9! + 9! + 9! + 9! + 9! + 9! + 9! = 2,540,160, 7 digits, seems to work, let's try another one
9! + 9! + 9! + 9! + 9! + 9! + 9! + 9! = 2,903,040, 7 digits again, too small, so, the upper limit is 7*9! 

*/

import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Euler {

    public static void main(String[] args) {

        var l = new HashMap<String, Integer>();
        IntStream.range( 0, 10 ).forEach( i -> l.put( String.valueOf( i ), i == 0 ? 1 : i * l.get( String.valueOf( i - 1 ) ) ) );
        System.out.println( IntStream.range( 3, 7 * l.get( "9" ) ).filter( i -> Stream.of( String.valueOf( i ).split( "" ) ).map( l::get ).reduce( 0, Integer::sum ) == i ).sum() );
    }
}
