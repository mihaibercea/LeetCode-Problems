# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

def letterCombinations(digits):

    l = len(digits)

    d = {}

    d['2'] = ['a', 'b', 'c']
    d['3'] = ['d', 'e', 'f']
    d['4'] = ['g', 'h', 'i']   
    d['5'] = ['j', 'k', 'l']
    d['6'] = ['m', 'n', 'o']
    d['7'] = ['p', 'q', 'r', 's']
    d['8'] = ['t', 'u', 'v']
    d['9'] = ['w', 'x', 'y', 'z']

    res = []

    curr = ''

    def backtrack(curr, digit_index=0):
        
        if len(curr)==len(digits):
                res.append(curr)
                return
        
        else:
            for letter in d[digits[digit_index]]:
                curr+=letter
                backtrack(curr, digit_index+1)
                curr = curr[:len(curr)-1]
            
    backtrack(curr)

    return res

# def letterCombinations1(digits):

#     l = len(digits)

#     d = {}

#     d['2'] = ['a', 'b', 'c']
#     d['3'] = ['d', 'e', 'f']
#     d['4'] = ['g', 'h', 'i']   
#     d['5'] = ['j', 'k', 'l']
#     d['6'] = ['m', 'n', 'o']
#     d['7'] = ['p', 'q', 'r', 's']
#     d['8'] = ['t', 'u', 'v']
#     d['9'] = ['w', 'x', 'y', 'z']

#     res = []

#     curr = ''

#     for digit in digits:
#         for letter in d[digit]:
#             curr+=letter
#             if len[curr] == len[digits]:
#                 res.append(curr)
            
#             curr = curr[:len(curr)-1]


digits = "23"

print(letterCombinations(digits))