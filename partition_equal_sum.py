class solution:


    def sol(self, num, k):
        table = []
        if not num or len(num) == 0:
            return False
        n = len(num)
        summation = 0
        # store the cumulative sum
        for i in xrange(n):
            summation += num[i]
            table.append(summation)

        # find whether there exists the desiring four nums
        
        for j in xrange(len(table)):
            p = 1
            curr = table[j]
            while p <= k:
                if curr*p in table:
                    p += 1
                else:
                    break
            if p == k + 1:
                return True
    
        return False
        


def backtrack(nums, res, temp):
    n = len(temp)
    if n == 4:
        s = ''
        for i in temp:
            s += str(i)
        if s not in res:
            res.append(s)
        return 
    
    for i in xrange(len(nums)):
        if n == 0:
            if nums[i] > 2:
                continue
        elif n == 1:
            if temp[-1] == 2 and nums[i] > 3:
                continue
        elif n == 2:
            if nums[i] > 5:
                continue
        new_nums =  nums[:i] + nums[i+1:]
        backtrack(new_nums, res, temp+[nums[i]])
        


def findMax(nums):
    larger_than_five = 0
    smaller_than_three = 0
    for i in nums:
        if i > 5:
            larger_than_five += 1
        if i < 3:
            smaller_than_three += 1
    if larger_than_five > 1 or smaller_than_three < 1:
        return []
    MAX = 0
    res_list = []
    idx = -1
    backtrack(nums, res_list, [])
    for i in xrange(len(res_list)):
        if int(res_list[i]) > MAX:
            MAX = int(res_list[i])
            idx = i
    res = res_list[idx]
    print res_list

    return res[:2]+':'+res[2:]



if __name__ == '__main__':
    #s = solution()
    #num = [2,3,1,1,2,3]
    #res = s.sol(num, 3)
    #print res
    nums = [0,0,5,9]
    print findMax(nums)

