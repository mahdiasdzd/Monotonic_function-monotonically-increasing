"""4. By using dynamic programming, provide procedure and solution for the alignment of the following sequences :

 CFVLVLTQSSIFSLL 
 CIFILSIDYALDYEL
 
 match = 3, miss = 0, gap = -2"""





#step 1 : our data
seqA = "CFVLVLTQSSIFSLL"
seqB = "CIFILSIDYALDYEL"


match = 3
mismatch = 0
gap = -2

#step 2 : creat a matrix with our sequences
row = len(seqA)
col = len(seqB)


#step 3 : turn into new value
def new_value(curI,curJ):
    if curI == row-1 or curJ == col-1:
        return A[curI][curJ]
    else:
        maxCell = A[curI+1][curJ+1]
        
        for i in range(curI+1,row):
            maxCell = max(maxCell,A[i][curJ]+gap)
        for j in range(curJ+1,col):
            maxCell = max(maxCell,A[curI][j]+gap)
        return A[curI][curJ] + maxCell


#step 4 : setup matrix 
def create_matrix(row,col,mismatch):
    A = [mismatch] * row
    for i in range(row):
        A[i] = [mismatch] * col
    return A


#step 5 : creat matrix with our data
def initialize_matrix(row,col,seqA,seqB,match):
    for i in range(row):
        for j in range(col):
            if seqA[i] == seqB[j]:
                A[i][j] = match
    return A


#step 6 : pass and push our new matrix with our data to show it
def complete_matrix(row,col,gap):
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            A[i][j] = new_value(i,j)
    return A


#step 7 : show the matrix
def print_matrix():
    for i in range(row):
        print("{}".format(A[i]))


#step 8 : creat a trace back to hold the script stable
def trace_back(i,j,action):
    if i == row-1 or j == col-1:
        return [seqA[i],seqB[i]]
    else:
        max_trace = max(A[i+1][j+1],A[i][j+1],A[i+1][j])
        if A[i+1][j+1] == max_trace:
            list = trace_back(i+1,j+1,"normal")
        elif A[i][j+1] == max_trace:
            list = trace_back(i,j+1,"skiprow")
        else:
            list = trace_back(i+1,j,"skipcol")
        
        partA = seqA[i]
        partB = seqB[j]
        if action == "skiprow":
            partA = "-"
        elif action == "skipcol":
            partB = "-"
        return [partA+list[0],partB+list[1]]


#step 9 : complete the matrix
def get_middle(traced):
    middle = ""
    for k in range(0,len(traced[0])):
        mid = " "
        if traced[0][k] == traced[1][k]:
            mid = "|"
        middle = middle + mid
    return middle






#step 10 : create initial grid
A = create_matrix(row,col,mismatch)

#step 11 : create initial matches
A = initialize_matrix(row,col,seqA,seqB,match)

A = complete_matrix(row,col,gap)

#step 12 : In order to show matrix.
print_matrix()

traced = trace_back(0,0,"normal")
middle = get_middle(traced)

#final step : show the result
print("{}\n{}\n{}".format(traced[0],middle,traced[1]))