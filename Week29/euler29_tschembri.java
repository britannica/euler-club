// Java :-/ 

import java.util.stream.*;

public class Main {

    public static void main(String[] args) {
	    System.out.println ( DoubleStream.iterate ( 2, i -> i + 1 ).limit ( 99 ).flatMap ( a -> IntStream.range ( 2, 101 ).mapToDouble ( b -> Math.pow ( a, b ) ) ).distinct ().count () );
    }
}
