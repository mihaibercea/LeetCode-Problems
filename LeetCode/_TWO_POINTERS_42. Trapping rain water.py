# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height):

    start = 0
    l=0
    bottom = 0
    r = 0

    peak_max = 0


    res = 0

    while l<len(height)-1 and r<len(height)-1:

        if height[l]<=height[l+1]:
            l+=1
        
        else:            
            r = l+1
            bottom = l+1

            while r<len(height)-1 and height[r]<height[l]:
                if height[r] > height[r-1]:
                    res+= min(height[r-1], h[r-bottom] - height[bottom]
                r+=1
                if bottom>r:
                    bottom = r
                elif r>bottom:
                    res +=   
                        
            if height[r]>=height[l]:
                for i in range(l, r):
                    res+= height[i] - bottom
                l=r
                bottom=r
        
                
    return res

height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height1))
