# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


from itertools import count


def minWindow(s, t):

    #contender = ''
    shortest = ''

    if len(s)<len(t):

        return shortest

    else:              

        count_t = {}

        for c in t:
            if c in count_t.keys():
                count_t[c]+=1
            else:
                count_t[c] = 1

        count_s = {}
        
        for c in s:
            if c in count_s.keys():
                count_s[c]+=1
            else:
                count_s[c] = 1

        for key in count_t.keys():
            
            if key not in count_s.keys():
                return shortest

            elif count_s[key] < count_t[key]:
                return shortest              
            
        shortest = s

        l = 0
        r = len(t)-1
        count = {}
        for c in s[l:r]:
            if c in count.keys():
                count[c]+=1
            else:
                count[c] = 1

        for l in range(len(s)-len(t)+1):

            if count[s[l]]<count_t[s[l]]:
                break

            while r<len(s):

                if s[r] in count.keys():
                    count[s[r]]+=1
                else:
                    count[s[r]] = 1

                for key in count_t.keys():                   
          
                    
                r+=1
            
            count


    return shortest


s1 = "aaaaaaaaaaaabbbbbcdd"
t1 = "abcd"

#print(s1[0:3])

print(minWindow(s1, t1))
                


# dict1 = {'a':1, 'b':2}
# dict2 = {'a':1, 'b':3}

# dict3 = dict1.items()&dict2.items()

# print(dict3)
    
