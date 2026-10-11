# miniCTF - Reverse Engineering Challenges

A beginner-friendly CTF challenge set focused on **Reverse Engineering**, created by **[becem69](https://becem69.github.io)**. Six challenges walk you through the core skills of the discipline: running binaries, reading strings, using a debugger, decompiling, reading source code, and reversing obfuscation.

All challenges use the flag format `Spark{...}`.

---

## Challenges

| # | Name | Category | Difficulty | Topic |
|---|------|----------|------------|-------|
| 1 | [Run_Me](#1-run_me) | Reverse Engineering | Very Easy | Execute a binary |
| 2 | [top_sec](#2-top_sec) | Reverse Engineering | Very Easy | `strings` command |
| 3 | [use_gdb](#3-use_gdb) | Reverse Engineering | Easy | GDB runtime patching |
| 4 | [VAULT](#4-vault) | JavaScript / Reverse Engineering | Easy | Source code reading |
| 5 | [intro_to_obfuscation](#5-intro_to_obfuscation) | Python / Reverse Engineering | Easy | Deobfuscation |
| 6 | [use_ghidra_or_IDA](#6-use_ghidra_or_ida) | Reverse Engineering | Easy | Decompiler (Ghidra / IDA) |

---

## Challenge Details

### 1. Run_Me

> *They told me the flag was locked away in a heavily protected vault guarded by dragons and ancient curses. Turns out you just had to run the program.*

A Linux ELF binary that prints the flag directly to stdout. The goal is simply to give it execute permission and run it, no reversing required.

**Skills:** Basic Linux, executing binaries  
**Handout:** `Run_Me/Handout/Run_Me`

---

### 2. top_sec

> *The developer named it "top_sec" and felt very proud of themselves. They did not know that strings are forever.*

The flag is compiled into the binary as a plaintext string literal in the `.rodata` section. The `strings` command is all you need.

**Skills:** `strings`, ELF sections  
**Handout:** `top_sec/Handout/top_sec`

---

### 3. use_gdb

> *The bouncer at the club keeps saying "Access denied." no matter what you do. Good thing you know someone who can have a little... chat with him at runtime.*

The binary decodes the flag in memory but only prints it if an `is_authorized` function returns non-zero, and it always returns 0. GDB lets you patch the return value at runtime to bypass the check.

**Skills:** GDB, breakpoints, runtime patching, XOR encoding  
**Handout:** `use_gdb/Handout/use_gdb`

---

### 4. VAULT

> *Welcome to the vault. Nothing to see here. Move along. (There is absolutely something to see here. It is right there in the file.)*

A JavaScript file contains a `reveal()` function that is never called. Inside it, an array of character codes shifted by 5 encodes the flag. Reading the source and running (or reversing) the function recovers it.

**Skills:** JavaScript source reading, character code arithmetic  
**Handout:** `VAULT/Handout/VAULT.js`

---

### 5. intro_to_obfuscation

> *Someone renamed all their variables to combinations of O and 0 and thought they were a hacker.*

A Python script checks user input against a stored base64 string. Variable names are obfuscated with `O`/`0` combinations. Renaming them reveals the scrambling function (reverse + base64 encode), which can be trivially inverted.

**Skills:** Python source reading, base64, variable renaming  
**Handout:** `intro_to_obfuscation/Handout/intro_to_obfuscation.py`

---

### 6. use_ghidra_or_IDA

> *The binary takes a number as an argument. One number unlocks the flag. Good luck guessing. (Or just use a decompiler like a normal person.)*

The binary expects a magic number (`0x539` = 1337) as a command-line argument. If correct, it XOR-decodes a hardcoded byte buffer with key `0x42` and prints the flag. Decompiling with Ghidra or IDA makes both the magic number and the XOR key immediately visible.

**Skills:** Ghidra / IDA Pro, decompilation, XOR decoding, `atoi`  
**Handout:** `use_ghidra_or_IDA/Handout/use_ghidra_or_IDA`

---

## Repository Structure

```
final/
├── Run_Me/
│   ├── Handout/          # Binary given to participants
│   ├── challenge/        # Challenge description
│   ├── solver/           # Writeup and solve script
│   └── challenge.yml     # CTFd metadata
├── top_sec/
├── use_gdb/
├── VAULT/
├── intro_to_obfuscation/
└── use_ghidra_or_IDA/
```

Each challenge follows the same layout:
- `Handout/` - file(s) distributed to players
- `challenge/README.md` - challenge description, category, difficulty, and flag
- `solver/README.md` - full writeup with analysis and solution
- `solver/solve.*` - solve script (Python or Bash)
- `challenge.yml` - CTFd-compatible challenge definition

---

## Tools You'll Need

| Challenge | Tools |
|-----------|-------|
| Run_Me | Bash |
| top_sec | `strings` |
| use_gdb | GDB |
| VAULT | Node.js or Python |
| intro_to_obfuscation | Python |
| use_ghidra_or_IDA | [Ghidra](https://ghidra-sre.org/) or [IDA Free](https://hex-rays.com/ida-free/) |

---

## Author

**becem69** - [becem69.github.io](https://becem69.github.io)
