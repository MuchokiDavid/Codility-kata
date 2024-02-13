function findShortestWordLength(str) {
  // Split the string into an array of words
  const words = str.split(' ');

  // Initialize the shortest length with a large value
  let shortestLength = Infinity;

  // Iterate through each word to find the shortest length
  for (let i = 0; i < words.length; i++) {
    const currentLength = words[i].length;
    if (currentLength < shortestLength) {
      shortestLength = currentLength;
    }
  }

  // Return the shortest length
  return shortestLength;
}

// Example usage:
const inputString = "This is a simple example";
const shortestLength = findShortestWordLength(inputString);
console.log(shortestLength);