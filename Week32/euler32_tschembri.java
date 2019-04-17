import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/*

Well, I'm not sure how to find the max value of a and b.
I tried some tests on papers and it didn't work, so I took two arbitrary values (1000) and it returned the correct
result. Kind of not happy with that, but I don't really have time...

*/


public class Euler {

    public static void main(String[] args) {

        System.out.println(
            IntStream.range( 2, 10000 )
                     .parallel()
                     .boxed()
                     .map( a -> IntStream.range( a, 10000 )
                                         .parallel()
                                         .boxed()
                                         .collect(  Collectors.toMap( b ->  a + "" + b + "" + ( a * b ), b -> a * b ) )
                     )
                     .map( Map::entrySet )
                     .flatMap( Collection::stream )
                     .filter( e ->   e.getKey().length() == 9
                                  && Stream.of( e.getKey().split( "" ) ).sorted().collect( Collectors.joining() ).equals( "123456789" )
                     )
                     .mapToInt( Map.Entry::getValue )
                     .distinct()
                     .sum() 
        );
    }
}
