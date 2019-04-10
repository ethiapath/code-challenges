
console.log('hello')


// counting votes takes in an array of names and finds
// the most occuring name
//
//

function countVotes(votes) {
  // reduce the array into an obj
  // keep a counter 
  // array.sort numVotesect.entries to search for the highest value
  // use a Stack to keep track of the previously added names
  let numVotes = {};
  let winner;

  const voters = votes.reduce( (accVotes, vote) => {
    if (!(vote in accVotes)) {
      accVotes[vote] = 0;
    } 
    accVotes[vote]++;
  }, {});

  console.log(voters);

  for (let i = 0; i < votes.length; i++) {
    console.log(numVotes)
    if (!numVotes.hasOwnProperty(votes[i])) {
      numVotes[votes] = 0;
    } 
    numVotes[votes]++;
    // if numVotes[winner] is less or equal then numVotes[votes[i]]
    // then replace votes[i] if equal then 
    // if numVotes[winner] <= numVote[votes[i]] && winner < votes[i]
    // set winner to votes[i]
  }

  console.log(counting)


  return counting;
}
const votes = ['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael'];


countVotes(votes);  // should return 'michael'
