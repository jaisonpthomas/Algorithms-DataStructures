#Code based (with several modifications) from GeeksforGeeks.com
#https://www.geeksforgeeks.org/longest-common-subsequence/

#Test example from Tushar Roy
#https://www.youtube.com/watch?v=NnD96abizww&index=3&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&t=0s

# Dynamic Programming implementation of LCS problem
 
def lcs(X , Y):
    row = len(Y)
    col = len(X)
 
    L = [[None]*(col+1) for i in range(row+1)]
 
    for r in range(row+1):
        for c in range(col+1):
            if r == 0 or c == 0 :
                L[r][c] = 0
            elif Y[r-1] == X[c-1]:
                L[r][c] = L[r-1][c-1]+1
            else:
                L[r][c] = max(L[r-1][c] , L[r][c-1])

    return L, L[r][c]
 
 
######TEST#######
C = "abcdaf"
R = "acbcf"
matrix, LCSlength = lcs(C, R)

ssCharList = []

r, c = len(matrix)-1, len(matrix[0])-1

while r > -1 and c > -1:
    if matrix[r][c] != matrix[r-1][c] and matrix[r][c] != matrix[r][c-1]:
        ssCharList.append(R[r-1])
        r -=1
        c -=1
    elif matrix[r][c] == matrix[r-1][c]:
        r-= 1
    else:
        c -= 1