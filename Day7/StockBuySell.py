def StockBuySell(prices):
    minsofar=prices[0]
    res=0
    n=len(prices)
    for i in range(1,n):
        minsofar=min(minsofar,prices[i])
        res=max(res,prices[i]-minsofar)
    return res;
        
        
prices = [7,10,1,3,6,9,2]
print(StockBuySell(prices))