"""
Hack Assembler - Raunak Kumar
Capstone Part B. Extra feature for K=77: warn when a label is repeated.
Usage: python assembler.py input.asm [output.hack]
"""
import re
import sys
from pathlib import Path

PREDEFINED = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}
for i in range(16):
    PREDEFINED[f"R{i}"] = i

COMP = {
    "0":"0101010", "1":"0111111", "-1":"0111010",
    "D":"0001100", "A":"0110000", "M":"1110000",
    "!D":"0001101", "!A":"0110001", "!M":"1110001",
    "-D":"0001111", "-A":"0110011", "-M":"1110011",
    "D+1":"0011111", "A+1":"0110111", "M+1":"1110111",
    "D-1":"0001110", "A-1":"0110010", "M-1":"1110010",
    "D+A":"0000010", "D+M":"1000010", "D-A":"0010011",
    "D-M":"1010011", "A-D":"0000111", "M-D":"1000111",
    "D&A":"0000000", "D&M":"1000000", "D|A":"0010101",
    "D|M":"1010101"
}
DEST = {"":"000","M":"001","D":"010","MD":"011","A":"100",
        "AM":"101","AD":"110","AMD":"111"}
JUMP = {"":"000","JGT":"001","JEQ":"010","JGE":"011",
        "JLT":"100","JNE":"101","JLE":"110","JMP":"111"}
SYMBOL = re.compile(r"^[A-Za-z_.$:][A-Za-z0-9_.$:]*$")

def clean_source(path):
    result = []
    with open(path, encoding="utf-8") as f:
        for no, raw in enumerate(f, 1):
            line = raw.split("//", 1)[0].strip()
            line = "".join(line.split())
            if line:
                result.append((no, line))
    return result

def first_pass(lines):
    symbols = PREDEFINED.copy()
    instructions = []
    pc = 0
    for no, line in lines:
        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]
            if not SYMBOL.fullmatch(label):
                raise ValueError(f"Line {no}: invalid label")
            if label in symbols:
                print(f"Warning: Line {no}: duplicate label '{label}' (first definition kept)")
            else:
                symbols[label] = pc
        else:
            instructions.append((no, line))
            pc += 1
    return symbols, instructions

def encode_a(value, no, symbols, next_var):
    if value.isdigit():
        address = int(value)
    else:
        if not SYMBOL.fullmatch(value):
            raise ValueError(f"Line {no}: invalid instruction")
        if value not in symbols:
            symbols[value] = next_var[0]
            next_var[0] += 1
        address = symbols[value]
    if not 0 <= address <= 32767:
        raise ValueError(f"Line {no}: A-instruction address out of range")
    return format(address, "016b")

def encode_c(line, no):
    if line.count(";") > 1:
        raise ValueError(f"Line {no}: invalid instruction")
    left, sep, jump = line.partition(";")
    if left.count("=") > 1:
        raise ValueError(f"Line {no}: invalid instruction")
    dest, eq, comp = left.partition("=")
    if not eq:
        comp, dest = dest, ""
    if dest not in DEST or comp not in COMP or jump not in JUMP:
        raise ValueError(f"Line {no}: invalid instruction")
    return "111" + COMP[comp] + DEST[dest] + JUMP[jump]

def assemble(input_path, output_path=None):
    lines = clean_source(input_path)
    symbols, instructions = first_pass(lines)
    code, next_var = [], [16]
    for no, line in instructions:
        if line.startswith("@"):
            if len(line) == 1:
                raise ValueError(f"Line {no}: invalid instruction")
            bits = encode_a(line[1:], no, symbols, next_var)
        else:
            bits = encode_c(line, no)
        code.append(bits)
    output_path = Path(output_path) if output_path else Path(input_path).with_suffix(".hack")
    output_path.write_text("\n".join(code) + "\n", encoding="utf-8")
    print(f"Assembly successful: {len(code)} instructions -> {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python assembler.py input.asm [output.hack]")
        raise SystemExit(2)
    try:
        assemble(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)
    except (OSError, ValueError) as exc:
        print(exc)
        raise SystemExit(1)
