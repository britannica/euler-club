#include <stdio.h>
#include <stdlib.h>

long target_number = 600851475143;

long* primes;
long number_of_prime_factors = 0;

int push_prime(long new_prime) {
    primes = realloc(primes, sizeof *primes);
    primes[number_of_prime_factors] = new_prime;
    number_of_prime_factors++;
    return 1;
}

int is_factor(long x, long y) {
    return x % y == 0;
}

int is_new_prime_factor(long num) {
    for(long i=0; i < number_of_prime_factors; i++) {
        if(num == primes[i] || is_factor(num, primes[i])) {
            return 0;
        }
    }
    return 1;
}

int is_factorization_complete() {
    long current_factor_product = 1;
    for(int i=0; i < number_of_prime_factors; i++) {
        current_factor_product *= primes[i];
    }
    if(current_factor_product == target_number) {
        return 1;
    }
    return 0;
}

int main() {
    primes = malloc(0);
    for (long i=2; i < target_number; i++) {
        if(is_factor(target_number, i) && is_new_prime_factor(i)) {
            push_prime(i);
            if(is_factorization_complete()) {
                printf("largest prime: %ld\n", primes[number_of_prime_factors-1]);
                return 1;
            }
        }
    }
    printf("no prime factors found; input is prime");
    return 0;
}
