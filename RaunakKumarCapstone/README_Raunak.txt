NAND TO TETRIS CAPSTONE - RAUNAK KUMAR
Roll No.: 2601411077
Programme: B.Tech CSE (Cyber Security), 2nd Year, 3rd Semester
Personal number K: 77

PART A - Computer
CPU.hdl, Memory.hdl and Computer.hdl are in Part_A/. Open them with the nand2tetris Hardware Simulator and run the official test scripts:
CPU.tst, Memory.tst, ComputerAdd.tst, ComputerMax.tst, ComputerRect.tst.
The supplied reference archive did not include all official .tst files or a Computer.hdl test screenshot; obtain these from the course project files and capture your own results.

PART B - Assembler
Run from a terminal:
  python Part_B/assembler.py Part_B/Add.asm
Or:
  python Part_C/assembler.py Part_C/Box.asm
The assembler performs two passes, resolves labels, allocates variables from RAM address 16, and translates A/C instructions.
K mod 3 = 77 mod 3 = 2, so the required extra feature is a warning for repeated labels.

PART C - Box
K mod 4 = 1, therefore width = 16 * (1 + 1) = 32 pixels.
The box starts at row 77, is 20 rows tall, and is drawn from the left edge.
SCREEN address = 16384 + (32 * 77) = 18848.
Run Box.hack in the CPU Emulator. Press any key to draw; release it to erase.

Note: Screenshots in Screenshots/ are retained from the supplied reference archive. Replace/retake them using your own simulator runs before submission. Do not present reference screenshots as your own work.

ADDED K-DEPENDENT VISUALS
- Part_B/Assembler_K77_Run.png: actual run of the Python assembler against a duplicate-label test input, showing the required warning.
- Part_C/Box_K77_Expected_Preview.png: expected geometry preview for K=77 (not an emulator screenshot).
The original reference screenshots have not been altered to falsely represent a new simulator run.
