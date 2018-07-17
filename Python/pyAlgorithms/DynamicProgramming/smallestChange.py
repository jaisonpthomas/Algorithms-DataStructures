#Code based from ByteByByte Tutorial (converted here into Python)
#https://www.youtube.com/watch?v=qH7fVuYlOOc&t=693s

def changeDynamic(x, coins):
    cache = []
    for i in range(x):
        cache.append(-1)
    return changeDynamic2(x, coins, cache)

def changeDynamicHelper(x, coins, cache):
    if x == 0:
        return 0
    
    min = x
    for coin in coins:
        if (x - coin) >= 0:
            if cache[x - coin] >= 0:
                c = cache[x - coin]
            else:
                c = changeDynamicHelper(x - coin, coins, cache)
                cache[x - coin] = c
            
            if min > (c+1):
                min = c + 1
                
    return min
           
myCoins = [1, 5, 10, 25]
print(changeDynamic(32, myCoins))
