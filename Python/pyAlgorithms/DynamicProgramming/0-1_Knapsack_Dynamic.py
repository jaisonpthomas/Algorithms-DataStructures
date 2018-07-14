#taken (with modidfications) from GeeksforGeeks.com
#https://www.geeksforgeeks.org/knapsack-problem/

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:      #elif: is the item you're considering weigh
                                    #in the range of weight being currently considered in col w?
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
                                #up and back(taking)       vs   row above (not taking)
                                            #if you take it/not you have to consider: value of item +
                                            #any remaining capacity you can use (go up and back)
                                            #max (compare just going up (not taking) against taking the item
                                                #and using remaining (up and back))
            else:                   #else: if not - just take the val in row above
                K[i][w] = K[i-1][w]
 
    return K, K[n][W]

# To test above function
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7
n = len(val)
matrix, outcome = (knapSack(W , wt , val , n))

i, j = len(matrix)-1, len(matrix[0])-1

itemsbyVal = []

while j > 0:
    if matrix[i][j] == matrix[i-1][j]:
        i = i - 1
    else:
        itemsbyVal.append(val[i-1])
        j -= wt[i-1]
        i -= 1