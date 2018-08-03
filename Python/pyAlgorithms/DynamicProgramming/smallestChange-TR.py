def minChange(coins, total):
    numCoins = [0] + [float('inf')]*total
    coinsForEachTotal = [-1]*(total+1)

    for coin in coins:
        for i in range(1, total+1):
            if coin <= i:
                if (1+numCoins[i-coin]) < numCoins[i]:
                    numCoins[i] = 1 + numCoins[i - coin]
                    coinsForEachTotal[i] = coin

    coinsUsed = []
    i = total
    while i > 0:
        coinsUsed.append(coinsForEachTotal[i])
        i -= coinsForEachTotal[i]

    return numCoins[total], coinsUsed

coins = [7, 2, 3, 6]
total = 13

numCoins, coinsUsed = minChange(coins, total)