// Raunak Kumar | Roll No. 2601411077 | K = 77
// Box: starts at row 77, 20 rows tall, 32 pixels wide (2 words).
// While any key is pressed draw black; otherwise erase.

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JNE
    @ERASE
    0;JMP

(DRAW)
    @18848
    D=A
    @addr
    M=D
    @20
    D=A
    @count
    M=D

(DRAW_LOOP)
    @addr
    A=M
    M=-1
    @addr
    D=M
    @1
    A=D+A
    M=-1
    @32
    D=A
    @addr
    M=D+M
    @count
    M=M-1
    D=M
    @DRAW_LOOP
    D;JGT
    @LOOP
    0;JMP

(ERASE)
    @18848
    D=A
    @addr
    M=D
    @20
    D=A
    @count
    M=D

(ERASE_LOOP)
    @addr
    A=M
    M=0
    @addr
    D=M
    @1
    A=D+A
    M=0
    @32
    D=A
    @addr
    M=D+M
    @count
    M=M-1
    D=M
    @ERASE_LOOP
    D;JGT
    @LOOP
    0;JMP
