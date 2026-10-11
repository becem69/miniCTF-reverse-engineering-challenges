# Writeup - top_sec

**Author: becem69 😝**

## Summary

The binary stores the flag as a plaintext string in its read-only data section (`.rodata`). The `strings` command extracts all printable sequences from a binary, making the flag immediately visible.

## Analysis

Running the binary:

```
$ ./top_sec
hi
```

Nothing useful. But the flag is compiled directly into the binary as a string literal. The `main` function just calls `puts` on a string at a fixed address in `.rodata`.

## Solution

```bash
strings top_sec | grep Spark
```

Output:

```
Spark{7h47s_imp0ssibl3_y0u_f0und_7h3_fl4g!!!}
```

Or simply:

```bash
strings top_sec
```

And look for the flag format among the output.

## Flag

`Spark{7h47s_imp0ssibl3_y0u_f0und_7h3_fl4g!!!}`
