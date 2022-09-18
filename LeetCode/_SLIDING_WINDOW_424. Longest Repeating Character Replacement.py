# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

             

def characterReplacement(s, k):
    
    x = 0     

    longest = 1
    contender = 1
   

    while x<len(s):
        
        rest = k
        
        #start = x        
            
        r = x+1
        
        while r <len(s) and rest>=0:                        
            
            if s[r]!=s[x]:
                
                rest-=1
                             
            # elif s[r]!=s[start]:
            #     rest-=1
            #     if rest < 0:                    
            #         break

            if rest >=0:
                contender = len(s[x: r+1])

                if longest<contender:
                    longest = contender

            r+=1        

        if r == len(s) and rest>=0:

            l = x-1

            while l >= 0 and rest >=0: 
                             
                if s[l]!=s[x]:
                    rest-=1                    
            
                if rest >=0:
                    contender = len(s[l:])

                    if longest<contender:
                        longest = contender

                l-=1
        
        x+=1


    return longest

s1 = "ABAA"
k1 = 0

print(characterReplacement(s1, k1))

