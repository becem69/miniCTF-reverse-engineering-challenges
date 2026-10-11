#!/usr/bin/env python3
# Solver for VAULT.js
# Each char code in the array is shifted up by 5 to encode the flag

codes = [88, 117, 102, 119, 112, 128, 79, 88, 100, 54, 58, 100,
         115, 53, 60, 100, 107, 53, 119, 100, 124, 56, 103, 100,
         53, 115, 113, 126, 130]

flag = ''.join(chr(c - 5) for c in codes)
print(flag)
