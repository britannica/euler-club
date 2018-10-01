; Euler9 in i386 assembler
; can be tested @http://www.tutorialspoint.com/compile_assembly_online.php
; system calls are for Linux. Should be replaced with int 21h in Windows.
; much much more verbose and uglier than 68000 assembler. Intel assemblers are awful. 

section    .text
    global _start       
    
_start:                    

    mov     eax,1          ; eax = outer loop index (a)
.l1:
    mov     ebx,1          ; ebx = inner loop inner (b)    
.l2:    
    mov     ecx,1000       ; 
    sub     ecx,ebx        ;
    sub     ecx,eax        ; c = 1000 - b - a
    
    push    eax            ; save eax
    push    ebx            ; save ebx    
    push    ecx            ; save ecx
    
    mul     eax            ; a = a * a
    
    push    eax            ; i386 is not orthogonal, multiplication requires eax, save eax again :-(

    mov     eax,ebx        ;
    mul     ebx            ; b = b * b
    mov     ebx,eax        ; 
    
    mov     eax,ecx        ;
    mul     ecx            ; c = c * c
    mov     ecx,eax        ;
    
    pop     eax            ; restore a
    
    add     eax,ebx        ; a = a + b
    sub     eax,ecx        ; a = a - c    
    cmp     eax,0          ; if ( a + b - c == 0 ) then 
    je      .found         ; found the values -> will display them
    
    pop     ecx            ; restore ecx
    pop     ebx            ; restore ecx
    pop     eax            ; restore eax

    inc     ebx            ; loop b until b == 1000
    cmp     ebx,1000
    jle     .l2

    inc     eax            ; loop a until a == 1000
    cmp     eax,1000
    jle     .l1
    
; found the values, will display them    
    
.found:
    pop     ecx            ; restore previously saved c
    pop     ebx            ; b    
    pop     eax            ; a
    
    call    _printDec      ; display a ( parameter is eax )
    push    eax            ; save a
    mov     eax,ebx        ; set function parameter
    call    _printDec      ; display b
    mov     eax,ecx        ; set function parameter
    call    _printDec      ; display c
    pop     eax            ; restore a
    
    mul     ebx            ; a = a * b
    mul     ecx            ; a = a * c
    call    _printDec      ; display product
    
    mov     eax, 1         ; system call number (sys_exit)
    int     0x80           ; call kernel

; display a number contained in the eax register

_printDec:

    section .bss

.decstr        resb  10
.ct1           resd  1      ; to keep track of the size of the string

    section .text
    
    pushad                  ; save all registers

    mov     dword[.ct1],0   ; assume initially 0
    mov     edi,.decstr     ; edi points to decstring
    add     edi,9           ; moved to the last element of string
    xor     edx,edx         ; clear edx for 64-bit division

.whileNotZero:
    mov     ebx,10          ; get ready to divide by 10
    div     ebx             ; divide by 10
    add     edx,'0'         ; converts to ascii char
    mov     byte[edi],dl    ; put it in sring
    dec     edi             ; mov to next char in string
    inc     dword[.ct1]     ; increment char counter
    xor     edx,edx         ; clear edx
    cmp     eax,0           ; is remainder of division 0?
    jne     .whileNotZero   ; no, keep on looping

    inc     edi             ; conversion, finish, bring edi
    
    ; print number
    
    mov     ecx, edi        ; back to beg of string. make ecx
    mov     edx, [.ct1]     ; point to it, and edx gets # chars
    mov     eax, 4          ; and print!
    mov     ebx, 1
    int     0x80
    
    ; print carriage return
    
    mov        edx, 1        ; message length
    mov        ecx, cr       ; message to write
    mov        ebx, 1        ; file descriptor (stdout)
    mov        eax, 4        ; system call number (sys_write)
    int        0x80          ; call kernel                

    popad                    ; restore all registers

    ret
    
    section    .data

cr    db    0xa              ;cr
