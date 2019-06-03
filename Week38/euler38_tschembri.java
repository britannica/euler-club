/*
Euler 38 in Java
We stop at 9999 because concatenating two 5 digit numbers will give a 10 digit number (which can't be pandigital)
*/

import java.time.*;
import java.util.*;
import java.util.stream.*;

public class Euler {

    public static void main(String[] args) {

        Instant start = Instant.now();
        System.out.println(
            IntStream.range( 1, 10000 )
                     .boxed()
                     .map ( i -> { int n = 1; String m = ""; while ( ( m += ( i * n++) ).length() < 9 ); return m; } )
                     .filter( m -> Stream.of( m.split( "" ) ).sorted().collect( Collectors.joining() ).equals( "123456789" ) )
                     .max( Comparator.naturalOrder() ).get()
        );
        System.out.println( String.format( "%dms", Duration.between( start, Instant.now() ).toMillis() ) );
    }
}


// --- output

// Connected to the target VM, address: '127.0.0.1:65092', transport: 'socket'
// 932718654
// 127ms
// Disconnected from the target VM, address: '127.0.0.1:65092', transport: 'socket'
//
// Process finished with exit code 0
