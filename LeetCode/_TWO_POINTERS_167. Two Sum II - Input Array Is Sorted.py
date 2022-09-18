

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

#def getIndices(numbers, target, back, forth)

from tkinter import N
from tkinter.tix import TixWidget


def twoSum(numbers, target):
        
    front = 0
    back = len(numbers) - 1

    res = []

    sum = numbers[front] + numbers[back]

    while sum != target:
        if numbers[front] + numbers[back] > target:
            back = back-1
            sum = numbers[front] + numbers[back]
            
        elif numbers[front] + numbers[back] < target:
            front = front +1

            sum = numbers[front] + numbers[back]

    res.append(front+1)
    res.append(back+1)
    return res

numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [-1, 1, 2, 3, 6, 11]
target2 = 7

print(twoSum(numbers2, target2))