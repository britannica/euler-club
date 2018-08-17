#include <stdio.h>
#include <stdlib.h>

long target_number = 600851475143;

long* primes;
long number_of_unique_prime_factors = 0;

int is_factor(long x, long y) {
    return x % y == 0;
}

int push_prime_and_reduce_target_number(long new_prime) {
    primes = realloc(primes, sizeof *primes);
    primes[number_of_unique_prime_factors] = new_prime;
    number_of_unique_prime_factors++;
    while(is_factor(target_number, new_prime)) {
        target_number = target_number / new_prime;
    }
    return 1;
}

int main() {
    primes = malloc(0);
    for (long i=2; i <= target_number; i++) {
        if(is_factor(target_number, i)) {
            push_prime_and_reduce_target_number(i);
        }
    }
    printf("largest prime: %ld\n", primes[number_of_unique_prime_factors-1]);
    return 0;
}
