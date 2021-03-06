// Euler 18 in BCPL (Basic Combined Programing Language) - 1967
// Can be downloaded @https://www.cl.cam.ac.uk/~mr10/BCPL.html 

GET "libhdr"

LET start() = VALOF
{
    LET triangle_height = 15
    LET rows = TABLE                75,
                                  95, 64,
                                17, 47, 82,
                              18, 35, 87, 10,
                            20, 4,  82, 47, 65,
                          19, 1,  23, 75,  3, 34,
                        88, 2,  77, 73,  7, 63, 67,
                      99, 65,  4, 28,  6, 16, 70, 92,
                    41, 41, 26, 56, 83, 40, 80, 70, 33,
                  41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
                53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
              70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
            91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
          63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
         4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23;

    LET line_width = triangle_height - 1
    LET pos = 0
    FOR i = 1 TO triangle_height - 2 DO { pos := pos + i }
       
    WHILE line_width > 0 DO 
    {
        FOR i = 0 TO line_width - 1
        {
            rows[pos+i] := rows[pos+i] + max( rows[pos + i + line_width ], rows[pos + i + line_width + 1 ] )
        }
        line_width := line_width - 1
        pos := pos - line_width
    }
    
    {
        writef("%i2*n",rows!0)
    }    
}
AND max(a,b) = VALOF
{
    TEST a < b
    THEN RESULTIS b
    ELSE RESULTIS a
}

// --- screenshot:

ts@tschembri5520:/mnt/c/tmp/BCPL/cintcode$ cintsys

BCPL 32-bit Cintcode System (9 Feb 2018)
0.000> c b euler18
bcpl euler18.b to euler18 hdrs BCPLHDRS t32

BCPL (27 Nov 2018) 32 bit with the FLT feature
Code size =   644 bytes of 32-bit little ender Cintcode
0.000> euler18
1074
0.000>

