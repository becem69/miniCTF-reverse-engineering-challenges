#!/usr/bin/env python3
# Solver for intro_to_obfuscation
# The scramble function is: base64(reverse(flag))
# So to reverse it: reverse(base64decode(stored))

import base64

stored = "fXk1NDNfNTFfbjAxNzRjNXVmYjBfMDdfMHI3bjF7a3JhcFM="
flag = base64.b64decode(stored).decode()[::-1]
print(flag)
