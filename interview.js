// bottom up algorithm: compute the answer for small values
// of amount first then use those answers to iteratively
// compute the answer for higher values until arriving at the final amount:
function change(amount, denominations) {
  // below: the index is the amount and the value
  // at each index is the number of ways
  // of getting that amount
  let waysOfDoingNCents = [];
  // initialize an array of zeros with indices
  // up to amount
  for (let i = 0; i <= amount; i++) {
    waysOfDoingNCents[i] = 0;
  }
  console.log(waysOfDoingNCents)

  waysOfDoingNCents[0] = 1;

  denominations.forEach((coin) => {
    for(let higherAmount = coin; higherAmount <= amount; higherAmount++) {
      let higherAmountRemainder = higherAmount - coin;
      waysOfDoingNCents[higherAmount] += waysOfDoingNCents[higherAmountRemainder];
    }
  })
  return waysOfDoingNCents;
}
let amount = 4;
let denominations = [1,2,3];

console.log(change(amount, denominations))