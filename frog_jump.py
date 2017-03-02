
def validCross(river):
    stones = []
    # first store the index of the stones
    for i in xrange(len(river)):
        if river[i] == '*':
            stones.append(i)
    # to keep record of the already visited combinations
    visited = set()
    # using backtrack to solve this problem
    def backtrack(pos, jump, target):
        if (pos, jump) in visited:
            return False
        if pos == target:
            return True
        if jump <= 0 or (pos not in stones):
            return False
        for j in [jump-1, jump, jump+1]:
            if backtrack(pos+j, j, target):
                return True
        visited.add((pos,jump))
        return False
    return backtrack(1, 1, stones[-1])

print validCross("***  *")





        