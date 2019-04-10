/*
Time Planner
Implement a time planner that receives the availability of two people and a duration. The time planner should return the earliest time slot that matches the given duration where both people have availability. If there is no common time slot that satisfies these requirements, return an empty array.

Each person's availability will be an array of two-element arrays. Each two-element array's first element represents the start time of a time slot, and the second array element represents the end time of that time slot. The input variable duration is a positive integer that represents the duration of a meeting in seconds. The output should be an array with the appropriate start time and end time that meets all of the requirements.

Analyze the time and space complexity of your solution.

Examples:

input: a = [[10, 50], [60, 120], [140, 210]]       
       b = [[0, 15], [60, 70]]         
       duration = 8 
output: [60, 68]

input: a = [[10, 50], [60, 120], [140, 210]]
       b = [[0, 15], [60, 72]]
       duration = 12
output: [60, 72]

input: a = [[10, 50], [60, 120], [140, 210]]         
       b = [[0, 15], [60, 70]]         
       duration = 12 
output: [] // since there is no common slot
These example inputs are obviously not realistic input numbers for representing meeting times. Ideally the inputs would consist of Unix epoch timestamps, but those are very large numbers to have to type out over and over again, so we're just going to fake that part. If your function works with these faux inputs, it will work just fine with Unix timestamps.*/


const getMettingTime = (person1, person2, duration) => {
  // loop through all combinations
  // console.log(person1, person2, duration)

  for (let i = 0; i < person1.length; i++) {
    for (let x = 0; x < person2.length; x++) {
      // console.log(person1[i], person2[x])
      // const duration1 = person1[i][0] - person1[i][1] 
      // const duration2 = person2[x][0] - person2[x][1] 

      const minStartTime = Math.max(person1[i][0], person2[x][0])
      const minEndTime = Math.min(person1[i][1], person2[x][1])
      // console.log(minStartTime + duration, minEndTime)
      if (minStartTime + duration <= minEndTime) {
        // console.log(person1[i][0], person2[x][0])
        return [minStartTime, minStartTime + duration]
      }
    }
  }
  return []
}


a = [[10, 50], [60, 120], [140, 210]]       
b = [[0, 15], [60, 70]]         
       duration = 8 
// [60, 68]
console.log(getMettingTime(a, b, duration))
 a = [[10, 50], [60, 120], [140, 210]]
       b = [[0, 15], [60, 72]]
       duration = 12
//  [60, 72]

console.log(getMettingTime(a, b, duration))
 a = [[10, 50], [60, 120], [140, 210]]         
       b = [[0, 15], [60, 70]]         
       duration = 12 
console.log(getMettingTime(a, b, duration))