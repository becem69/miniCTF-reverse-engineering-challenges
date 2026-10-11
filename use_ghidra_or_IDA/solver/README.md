# Writeup - use_ghidra_or_IDA

**Author: becem69 😝**

## Summary

The binary expects exactly one argument. It compares the argument (converted to an integer with `atoi`) against the value `0x539` (1337). If they match, it XOR-decodes a hardcoded byte buffer with key `0x42` and prints the flag.

## Analysis

Running the binary with no arguments or a wrong number:

```
$ ./use_ghidra_or_IDA
Usage: ./use_ghidra_or_IDA <number>
$ ./use_ghidra_or_IDA 42
Nope.
```

Opening the binary in Ghidra or IDA and decompiling `main` gives the following output:

```c
undefined8 main(int param_1, undefined8 *param_2)
{
  int iVar1;
  undefined8 uVar2;
  byte local_28 [28];
  int local_c;

  local_28[0]    = 0x11;
  local_28[1]    = 0x32;
  local_28[2]    = 0x23;
  local_28[3]    = 0x30;
  local_28[4]    = 0x29;
  local_28[5]    = 0x39;
  local_28[6]    = 0x26;
  local_28[7]    = 0x71;
  local_28[8]    = 0x21;
  local_28[9]    = 0x72;
  local_28[10]   = 0x2f;
  local_28[0xb]  = 0x32;
  local_28[0xc]  = 0x2b;
  local_28[0xd]  = 0x2e;
  local_28[0xe]  = 0x71;
  local_28[0xf]  = 0x30;
  local_28[0x10] = 0x1d;
  local_28[0x11] = 0x2b;
  local_28[0x12] = 0x31;
  local_28[0x13] = 0x1d;
  local_28[0x14] = 0x75;
  local_28[0x15] = 0x2a;
  local_28[0x16] = 0x71;
  local_28[0x17] = 0x1d;
  local_28[0x18] = 0x29;
  local_28[0x19] = 0x71;
  local_28[0x1a] = 0x3b;
  local_28[0x1b] = 0x3f;

  if (param_1 == 2) {
    iVar1 = atoi((char *)param_2[1]);
    if (iVar1 == 0x539) {                           // 0x539 = 1337
      for (local_c = 0; local_c < 0x1c; local_c = local_c + 1) {
        putchar((uint)(local_28[local_c] ^ 0x42));  // XOR each byte with 0x42
      }
      putchar(10);
      uVar2 = 0;
    }
    else {
      puts("Nope.");
      uVar2 = 1;
    }
  }
  else {
    printf("Usage: %s <number>\n", *param_2);
    uVar2 = 1;
  }
  return uVar2;
}
```

Two things stand out:

1. The magic number is `0x539` which is `1337` in decimal.
2. Each byte in `local_28` is XORed with `0x42` to produce the flag characters.

We do not even need to run the binary. We can copy the bytes directly from the decompiler output and XOR them in Python.

## Solution

```bash
./use_ghidra_or_IDA 1337
```

Or compute the flag directly from the decompiler output:

```python
buf = [
    0x11, 0x32, 0x23, 0x30, 0x29, 0x39, 0x26, 0x71,
    0x21, 0x72, 0x2f, 0x32, 0x2b, 0x2e, 0x71, 0x30,
    0x1d, 0x2b, 0x31, 0x1d, 0x75, 0x2a, 0x71, 0x1d,
    0x29, 0x71, 0x3b, 0x3f,
]
print(''.join(chr(b ^ 0x42) for b in buf))
```

Output:

```
Spark{d3c0mpil3r_is_7h3_k3y}
```

## Flag

`Spark{d3c0mpil3r_is_7h3_k3y}`
