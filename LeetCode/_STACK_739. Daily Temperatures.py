# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

from tempfile import tempdir


def dailyTemperatures(temperatures):

    answer = [0] * len(temperatures)

    stack = []

    
    for i in range(len(temperatures)):
        stack.append([i, temperatures[i], 0])
                
        while len(stack)>=2 and stack[-2][1]<stack[-1][1]:
            answer[stack[-2][0]] = stack[-2][2]+1            
            del stack[-2]            

        if len(stack)>=2 and stack[-2][1]>=stack[-1][1]: 
            for j in range(len(stack)-1):
                stack[j][2] +=1

    for item in stack:
        answer[item[0]] = 0          

    return answer


temperatures = [89,62,70,58,47,47,46,76,100,70]
print(dailyTemperatures(temperatures))
