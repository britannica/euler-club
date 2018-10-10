import java.math.*;
public class prime {
    public static void main(String[] args) {

    Long total = new Long(2);
    for (int i=3; i<2000000; i+=2) {
    boolean isPrime = true;
    double squareroot = Math.sqrt(i);
        for (int j=2; j<=squareroot; j++){
            if (i % j == 0){ 
                isPrime = false;
                break;
            }
        }
        if(isPrime){
            total = total + i;
        }
    }
    System.out.println("Summation of primes up to 2,000,000  = "+total); 
}
}