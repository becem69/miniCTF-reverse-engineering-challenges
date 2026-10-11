# "import ... as" gives a module a nickname. Here, the base64 module
# is nicknamed _O0O. Base64 is a way to write data using only letters,
# numbers, +, / and = signs. Hint: strings ending in "=" often use it.
import base64 as _O0O

# This is the scrambled version of the secret flag.
# The program never stores the real flag, only this transformed text.
_0O0 = "fXk1NDNfNTFfbjAxNzRjNXVmYjBfMDdfMHI3bjF7a3JhcFM="

# A lambda is a tiny function. This one takes a string (_s) and:
#   1. _s[::-1]      -> flips the string backwards ("abc" becomes "cba")
#   2. .encode()     -> turns the text into bytes
#   3. b64encode()   -> converts those bytes to base64
#   4. .decode()     -> turns the result back into normal text
# Rename it to something readable, like "scramble", to make it easier to follow.
_OO0 = lambda _s: _O0O.b64encode(_s[::-1].encode()).decode()

# Ask the player for a guess and store it in the variable "_".
_ = input("Enter the flag: ")

# Scramble the guess with the function above and compare it to the stored text.
# If they match, the guess is the real flag.
print("Correct!" if _OO0(_) == _0O0 else "Nope.")
