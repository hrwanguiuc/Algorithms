
# Problem:
#   given a matrix M: M = [1,   2,  3]
#                         [4,   5,  6]
#                         [7,   8,  9]
#   return a new matrix I = [1,     3,      6]
#                           [5,     12,     21]
#                           [12,    27,     45]                          
#   diag sum       
def solution(M):
    # M is a matrix
    m = len(M)
    n = len(M[0])
    if m == 0:
        return []

    def summation(i,j):
        res = 0
        for k in xrange(j+1):
            res += M[i][k]
        return res

    I = [[0 for x in xrange(n)] for y in xrange(m)]
    I [0][0] = M[0][0]

    for i in xrange(1, n):
        I[0][i] = M[0][i] + I[0][i-1]
    for j in xrange(1, m):
        I[j][0] = M[j][0] + I[j-1][0]

    for i in xrange(1, m):
        for j in xrange(1, n):
            I[i][j] = I[i-1][j] + summation(i,j)

    return I

if __name__ == '__main__':
    M = [[1,2,3],[4,5,6],[7,8,9]]
    print solution(M)