""" LCS problem"""


def lcs(X, Y):


    #step 1 : returns the number of X and Y items
    m = len(X)
    n = len(Y)
  
    #step 2 :  creat dynamic programming value 
    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    
    return L[m][n]

  
  
#our input
X = "AGGTAB"
Y = "GXTXAYB"

#final step : show the result
print("Length of LCS is ", lcs(X, Y))
  
