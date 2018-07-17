def subsetSum(nums, total):
    """Given a list of numbers and a total to reach, subsetSum will return
    True if any subset of those numbers will add to the given total.
    Otherwise, will return False."""
    
    matrix = [ [1] + [0]*total for k in range(len(nums)+1)]
    
    for r in range(1, len(nums)+1):
        for c in range(1, total+1):
            if matrix[r-1][c] == 1:
                matrix[r][c] = 1
            else:
                subValue = c - nums[r-1]
                if matrix[r-1][subValue] == 1:
                    matrix[r][c] = 1
                else:
                    matrix[r][c] = 0           
    
    return bool(matrix[r][c])
            

alpha = subsetSum([1, 2, 4, 5, 9], 3)