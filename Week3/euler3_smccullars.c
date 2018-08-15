#include <stdio.h>
#include <stdlib.h>

long* primes;
long number_of_primes = 0;

int push_prime(long new_prime) {
    long old_number_of_primes = number_of_primes;
    number_of_primes++;
    long* new_primes = malloc(number_of_primes * sizeof(*primes));
    for(long i=0; i < old_number_of_primes; i++) {
        new_primes[i] = primes[i];
    }
    new_primes[old_number_of_primes] = new_prime;
    primes = new_primes;
    free(primes);
    return 1;
}

int is_factor(long x, long y) {
    return x % y == 0;
}

int is_prime(long num) {
    for(long i=0; i < number_of_primes; i++) {
        if(is_factor(num, primes[i])) {
            return 0;
        }
    }
    return 1;
}

int main() {
    primes = malloc(0);
    long target_number = 600851475143;
    for (long i=2; i < target_number; i++) {
        if(is_factor(target_number, i) && is_prime(i)) {
            push_prime(i);
            printf("%ld is a prime factor\n", i);
            long current_factor_product = 1;
            for(int j=0; j < number_of_primes; j++) {
                current_factor_product *= primes[j];
            }
            if(current_factor_product == target_number) {
                printf("largest prime: %ld\n", primes[number_of_primes-1]);
                return 1;
            }
        }
    }
    printf("no prime factors found; input is prime");
    return 0;
}
