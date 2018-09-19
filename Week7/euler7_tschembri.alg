# nth prime number in ALGOL68 #
# test online @http://www.tutorialspoint.com/execute_algol_online.php #
# uses the Eratosthenes sieve. #
# upper bound of sieve is ~ n log ( n log( n ) ) #

INT n = 10001;
INT max = ENTIER( n * ln( n * ln( n ) ) );
[max]BOOL sieve;

FOR i TO UPB sieve DO
    sieve[i] := TRUE
OD;

INT p := 2;
WHILE p*p <= max DO
    IF sieve[p] = TRUE THEN
        FOR i FROM p*2 BY p TO max DO
            sieve[i] := FALSE
        OD
    FI;
    p := p+1
OD;

INT c := 0;
INT i := 2;
WHILE i < max AND c < n DO
    IF sieve[i] = TRUE THEN
       c := c+1;
       p := i
    FI;
    i := i+1
OD;

print(p)
