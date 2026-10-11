# Writeup - intro_to_obfuscation

**Author: becem69 😝**

## Summary

The script stores a base64-encoded string and compares it against a scrambled version of your input. The scrambling function reverses the input string then base64-encodes it. To recover the flag, we reverse the process: base64-decode the stored string, then reverse the result.

## Analysis

Reading the source:

```python
import base64 as _O0O

_0O0 = "fXk1NDNfNTFfbjAxNzRjNXVmYjBfMDdfMHI3bjF7a3JhcFM="

_OO0 = lambda _s: _O0O.b64encode(_s[::-1].encode()).decode()

_ = input("Enter the flag: ")
print("Correct!" if _OO0(_) == _0O0 else "Nope.")
```

Renaming the obfuscated names:

```python
scramble = lambda s: base64.b64encode(s[::-1].encode()).decode()
```

So `scramble(flag) == stored`. To reverse:

```
flag = base64.b64decode(stored).decode()[::-1]
```

## Solution

```python
import base64

stored = "fXk1NDNfNTFfbjAxNzRjNXVmYjBfMDdfMHI3bjF7a3JhcFM="
flag = base64.b64decode(stored).decode()[::-1]
print(flag)
```

Output:

```
Spark{1n7r0_70_0bfu5c4710n_15_345y}
```

## Flag

`Spark{1n7r0_70_0bfu5c4710n_15_345y}`
