! Fortran77
! You can test it online at: https://www.onlinegdb.com/online_fortran_compiler (other online compilers don't support comments)

PROGRAM prime_factors

    IMPLICIT NONE;
    
    REAL(KIND=8) :: N=600851475143_8                ! KIND=8 and _8 extension: 64bit real 
    REAL(KIND=8) :: I = 3_8

10  IF  ( I .LE. SQRT( N ) ) THEN                   ! every composite number (more than 2 factors) has a prime factor <= to its square root 
20      IF  ( MODULO( N, I ) .EQ. 0 ) THEN          ! if n can be divided by i then i is a prime number 
            N = N / I                               ! divide n by the prime number
            GOTO 20                                 ! and loop until n can be divided by this prime number
        END IF                                      
        I = I + 2                                   ! I = I + 2: skip even numbers, prime numbers are always odd (except 2)
        GOTO 10                                     ! and restart
    END IF
    PRINT *, INT(N)                                 ! once divided by prime factors, n = largest prime factor

END PROGRAM prime_factors

! result is:
!  6857
