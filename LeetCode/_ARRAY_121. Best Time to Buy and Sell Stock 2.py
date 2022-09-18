# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
    maxProfit = 0
    maxprice = 0
    minprice = prices[0]
    coordmin = 0
    for i in range(len(prices)):
        if prices[i]>maxprice:
            maxprice = prices[i]
            coordmax = i
        if prices[i]<minprice:
            minprice = prices[i]
            coordmin = i        
    if coordmin<coordmax:
        return (maxprice - minprice)        
    else: 
        return max(maxProfit(prices[:coordmax]), maxProfit(prices[coordmax:]))
    
     
prices = [1,3,6,8,9,3,5,15]
prices2 = [2, 3, 9, 4, 1, 6]

print(maxProfit(prices))
print(maxProfit(prices2))
