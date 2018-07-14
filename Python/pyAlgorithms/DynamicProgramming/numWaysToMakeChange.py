#Code based from ONeill Code Tutorial
#https://www.youtube.com/watch?v=jaNZ83Q3QGc&t=239s

def numWaysToMakeChange(amount):
    coins = [1, 2, 5]    
    combinations = [1]
    for i in range(amount):
        combinations.append(0)
        
    for coin in coins:
        for i in range(1, len(combinations)):
            if i >= coin:
                combinations[i] += combinations[i - coin]
                
    return combinations[amount]
           

funcOutput = numWaysToMakeChange(12)
print(funcOutput)