'''
Given an array of integers where each element represents the maximum number of steps that can be made forward from that element, write a function to return the minimum number of jumps to reach the end of the array, starting from the first element. If an element is 0, then we cannot move through that element.

'''

def minjumps(arr):

    shortestJumps = []

    tempArr = []
    i = 0
    while i < len(arr):
        print(i, tempArr)
        largest_jump = 0
        for j in range(1, arr[i]):
            if arr[j] > largest_jump:
                print(i + arr[j], largest_jump)
                largest_jump = arr[j]
                tempArr.append(largest_jump)


        i = i + arr[i]


    return tempArr


print(minjumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

# make a var with shortest jumps
# find all possible combinations for jumps
# if combination is greater then the latest shortest array skip it
# replace a var with any new shorest array length
# store jump arrays
# find the array with shortest length

# Input: [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3   // going from 1 -> 3 -> 8 -> 9

