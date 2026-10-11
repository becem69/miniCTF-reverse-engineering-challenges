// This is all the program does when you run it.
console.log("Welcome to the vault.");
console.log("Nothing to see here, move along.");

// This function is NEVER called, so running the script never shows it.
// But it is still in the file. Anyone who reads the code can find it.
function reveal() {
  // Each number is a character code that was shifted up by 5.
  const codes = [88, 117, 102, 119, 112, 128, 79, 88, 100, 54, 58, 100, 115, 53, 60, 100, 107, 53, 119, 100, 124, 56, 103, 100, 53, 115, 113, 126, 130];

  let out = "";
  for (const c of codes) {
    // Shift each code back down by 5 and turn it into a character.
    out += String.fromCharCode(c - 5);
  }
  return out;
}
