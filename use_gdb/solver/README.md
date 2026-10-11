# Writeup - use_gdb

**Author: becem69 😝**

## Summary

The binary has a function called `is_authorized` that always returns 0 (false). The main function XOR-decodes the flag in memory but only prints it if `is_authorized` returns non-zero. We use GDB to patch the return value at runtime.

## Analysis

Running the binary gives:

```
Access denied.
```

Disassembling with `objdump` reveals:

```asm
is_authorized:
    mov eax, 0    ; always returns 0 (false)
    ret
```

In `main`, the flag bytes are XOR-decoded with key `0x37` into a buffer, then `is_authorized` is called. If it returns 0 the flag is never printed.

## Solution with GDB

```bash
gdb ./use_gdb
```

Inside GDB:

```
(gdb) break is_authorized
(gdb) run
(gdb) return 1
(gdb) continue
```

Or patch the return value of `eax` right after the call:

```
(gdb) break *0x4011a7
(gdb) run
(gdb) set $eax = 1
(gdb) continue
```

Output:

```
Spark{gdb_m4kes_it_3asy}
```

## Flag

`Spark{gdb_m4kes_it_3asy}`
