function columnNames(n) {
  if (n < 0) { return -1; }
  let result = [];
  let alphabets =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
  for (let i=0; i < n; i++){
    // Track the value of the index by the size of the alphabets
    let index = Math.floor(i/26);
    // Initiating the value that we will store in the result
    let item = []

    if(index > 0) {
       // precedent character
      let precedentChar = alphabets[index-1]
      item.push(precedentChar);
    }
    // Add the current Character
    let currentChar = alphabets[i%26];
    item.push(currentChar);

    // Turning item list into a string
    let str = item.join("");
    result.push(str);
     
  }

  return result.join(',');
}


console.log(columnNames(5));
console.log(columnNames(80));
