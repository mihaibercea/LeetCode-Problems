# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


def minEatingSpeed (piles, h):

    if len(piles) == 1:
        if piles[0]%h!=0:
            return piles[0]//h+1
        else:
            return piles[0]/h

    piles = sorted(piles)
       
    total = 0

    for pile in piles:
        total+=pile

    fastest = piles[-1]

    slowest = total//h if total&h==0 else total//h+1

    if slowest > fastest:
        return slowest

    optimal = slowest    

    ref = 0      

    for i in range(ref, len(piles)):
        if optimal>=piles[i]:
            i+=1
        else:
            ref = i
            break
   
    while ref<len(piles):

        actual_h = ref     
        for i in range(ref, len(piles)):            
            if piles[i]%optimal>0:
                actual_h+=piles[i]//optimal+1
            else:
                actual_h+=piles[i]//optimal

        if actual_h == h:
            return optimal

        if actual_h<h:

            r = piles[ref-1]
            l = piles[ref-2]            

            while r>l:
                actual_h = ref-1                
                optimal = (r+l)//2                

                for i in range(ref-1, len(piles)):            
                    if piles[i]%r>0:
                        actual_h+=piles[i]//optimal+1
                    else:
                        actual_h+=piles[i]//optimal
                if actual_h ==h:
                    return optimal

                actual_h = ref-1
                optimal = ((r+l)//2)+1
                for i in range(ref-1, len(piles)):            
                    if piles[i]%r>0:
                        actual_h+=piles[i]//optimal+1
                    else:
                        actual_h+=piles[i]//optimal
                if actual_h ==h:
                    return optimal

                if actual_h>h:
                    l = optimal                    
                if actual_h<h:
                    r = optimal
                    

        ref+=1
        optimal = piles[ref-1]
        
    return optimal
    
piles = [3,6,7,11]
h = 8

piles2 = [3, 5, 7, 19, 100]
h2 = 14
print(minEatingSpeed(piles2, h2))