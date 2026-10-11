# Writeup - VAULT

**Author: becem69 😝**

## Summary

The JavaScript file contains a `reveal` function that is never called at runtime. Inside it, an array of character codes each shifted up by 5 encodes the flag. Subtracting 5 from each code and converting to characters gives the flag.

## Analysis

Reading `VAULT.js`:

```js
function reveal() {
  const codes = [88, 117, 102, 119, 112, 128, 79, 88, 100, 54, 58, 100, 115, 53, 60, 100, 107, 53, 119, 100, 124, 56, 103, 100, 53, 115, 113, 126, 130];
  let out = "";
  for (const c of codes) {
    out += String.fromCharCode(c - 5);
  }
  return out;
}
```

Each number is a character code shifted up by 5. Shift them back down by 5 to get the real characters.

## Solution

Run the reveal function in Node.js:

```bash
node -e "
const codes = [88,117,102,119,112,128,79,88,100,54,58,100,115,53,60,100,107,53,119,100,124,56,103,100,53,115,113,126,130];
console.log(codes.map(c => String.fromCharCode(c - 5)).join(''));
"
```

Or in Python:

```python
codes = [88,117,102,119,112,128,79,88,100,54,58,100,115,53,60,100,107,53,119,100,124,56,103,100,53,115,113,126,130]
print(''.join(chr(c - 5) for c in codes))
```

Output:

```
Spark{JS_15_n07_f0r_w3b_0nly}
```

## Flag

`Spark{JS_15_n07_f0r_w3b_0nly}`
