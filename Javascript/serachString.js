/*
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
*/

function stringSearch(text){
     // Convert the input text to lowercase for case-insensitivity
  text = text.toLowerCase();
  // Create an empty object to store character counts
  const charCount = {};
  // Initialize a count variable to track the number of duplicates
  let duplicateCount = 0;

  for (const char of text) {
    if (char.match(/[a-z0-9]/)) {
      if (charCount[char]) {
        charCount[char]++;
        // Check if the character has occurred more than once
        if (charCount[char] === 2) {
          duplicateCount++;
        }
      } else {
        charCount[char] = 1;
      }
    }
  }
  return duplicateCount;
}