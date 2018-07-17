def rodCut(length, cutLenVals):
    dpMatrix = [ [0]*(length+1) for _ in range(len(cutLenVals)+1)]
    r = 0
    for cutLen in cutLenVals:
        r += 1
        for c in range(1, length+1):
            if c < cutLen:
                dpMatrix[r][c] = dpMatrix[r-1][c]
            else:
                dpMatrix[r][c] = max(dpMatrix[r-1][c], cutLenVals[cutLen] + dpMatrix[r][c-cutLen])

    return dpMatrix
    
cutVals = {2:3, 3:7, 1:2}
optionsMatrix = rodCut(5, cutVals)
for row in optionsMatrix: print(row)