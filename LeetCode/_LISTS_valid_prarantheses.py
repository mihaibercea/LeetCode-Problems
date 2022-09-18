# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
    
    s_list = list(s)  

    check1 = bool

    check = False

    l = len(s)

    tries = 0   

    def check_parity(s, tries):         

        if len(s)>0:                                  
            while tries < l and len(s)>0:        
                if s[0] == "(":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == ")":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == "[":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == "]":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == "{":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == "}":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == ")" or s[0] == "]" or s[0] == "}":
                    return False
                    break

               
        if len(s)==0:
            return True
        else:
            return False    

    def check_inside(s_list):

        l = len(s)

        tries1 = 0  

        inside_string = ""

        inside_string.join(s_list)

        if check_parity(inside_string, tries1):

            for x in range(len(s_list)):
                
                if s_list[x] ==  "(":
                    for y in range(x, len(s_list)):
                        if s_list[y] == ")":
                            inside = s_list[x+1:y]                        
                            if len(inside) == 0:
                                
                                check = True
                                break                                                                          
                            elif len(inside)>0:                            
                                if len(inside)%2 != 0:
                                    check = False
                                    break
                                check_inside(inside)


                if s_list[x] ==  "{":
                    for y in range(x, len(s_list)):
                        if s_list[y] == "}":
                            inside = s_list[x+1:y]                        
                            if len(inside) == 0:
                                
                                check = True
                                break                                                                          
                            elif len(inside)>0:                            
                                if len(inside)%2 != 0:
                                    check = False
                                    break
                                check_inside(inside)

                if s_list[x] ==  "[":
                    for y in range(x, len(s_list)):
                        if s_list[y] == "]":
                            inside = s_list[x+1:y]                        
                            if len(inside) == 0:
                                
                                check = True
                                break                                                                          
                            elif len(inside)>0:
                                if len(inside)%2 != 0:
                                    check = False
                                    break
                                check_inside(inside)
            
        else:
            check = False
            
        return check
    
    if check_parity(s, tries, check):
        return check_inside(s_list)        
    else:
        return False

print(isValid("[({])}")) 
           

        
        
