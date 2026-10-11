#!/usr/bin/env python3
# Solver for use_gdb
# Decodes the flag directly from the binary without needing GDB
import struct

# Three 8-byte chunks loaded into the stack buffer in main
b1 = struct.pack("<Q", 0x53504c5c45564764)
b2 = struct.pack("<Q", 0x6844525c035a6855)
b3 = struct.pack("<Q", 0x4a4e44560468435e)

raw = b1 + b2 + b3

# Each byte is XORed with 0x37 to produce the flag (24 bytes, loop runs 0..0x17)
flag = ''.join(chr(x ^ 0x37) for x in raw[:0x18])
print(flag)
