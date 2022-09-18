
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

def maxArea(height):

    l = 0
    # last = len(height)-1    
    r = len(height)-1

    # res = [0, 0]

    contender = 0
    largest = 0
       
    while l<r:

        contender = min(height[l], height[r])*(r-l)
        if contender > largest:
            largest = contender
            # res[0] = l
            # res[1] = r

        if height[l] >= height[r]:

           r-=1

        elif height[l] < height[r]:

            l+=1       

        
    return largest

                        
    # else:
    #     for i in range(half+1):

    #         if min(height[front+i], height[back])*(back-front-i) >  min(height[front], height[back])*(back-front):
    #             front = front +i

    #     for i in range(half+1):
    #         if min(height[front+i], height[back])*(back-front-i) >  min(height[front], height[back])*(back-front):
    #             back = back -i      

    # return (min(height[front], height[back]) * (back-front))
        

height1 = [2,3,4,5,18,17,6]
height2 = [1, 3, 2, 4, 9]
print(maxArea(height2))
print(maxArea(height1))

                

  


