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
            ir
        


def findMax(nums):
    
    MAX = 0
    res_list = []
    idx = -1
    backtrack(nums, res_list, [])
    if not res_list:
        return 'not valid'
    for i in xrange(len(res_list)):
        if int(res_list[i]) > MAX:
            MAX = int(res_list[i])
            idx = i
    res = res_list[idx]
    print res_listif

    return res[:2]+':'+res[2:]


def min_unsort_array(nums):
    n = len(nums)
    res = 0
    lo = n-1
    hi = 0
    # traverse the array to find the first element which is larger than the next element
    for i in xrange(n-1):
        if nums[i] > nums[i+1]:
            lo = i
            break
    # when the array is already sorted
    if lo == n-1:
        return 0
    # find the first element from right to left that is smaller than the next element
    for j in xrange(n-1, 1, -1):
        if nums[j] < nums[j-1]:
            hi = j 
            break

    # find the max and min value between lo and hi
    temp_min = min(nums[lo:hi+1])
    temp_max = max(nums[lo:hi+1])
    # find the max element in the left side of the lo in nums
    l_max_idx = 0
    l_max = nums[0]
    for i in xrange(lo):
        if nums[i] > l_max:
            l_max = nums[i]
            l_max_idx = i
    # find the min value at the right side of the hi in nums
    r_min_idx = n-1
    r_min = nums[n-1]
    for i in xrange(n-1, hi, -1):
        if nums[i] < r_min:
            r_min = nums[i]
            r_min_idx = i
    # compare that with the found one in nums[lo, hi]
    if l_max > temp_min:
        lo = l_max_idx
    if r_min < temp_max:
        hi = r_min_idx
    print hi
    print lo
    return hi-lo+1
'''
If you are given an array, most of them in a sorted order but a small portion of them is in unsorted order. 
Our task is to find the minimum length of the unsorted part, sorting which could make our array in a complete sorted order.
To find this portion of the array, we need to find scan this array from left to right to find the first element who is in a bad order, in other words, 
this element is larger than the next element. And keep the index of this element, which is denoted as low. Similary, we could scan from right to left
to find the first element who is in bad order, in other words, the first element who is smaller than the next element(which is the left side of this element since we are in reverse order)
The index is denoted as high.

Then, we could get a subarray of the original array, the boundary is low and high. And we know at least the elements between this part is unsorted. 
For example, the original array is [1,2,3,7,9,6,8,10,23], after finding the low and high index, we could separate the array into three parts:
[1,2,3] | 7,9,6 | 8,10,23]. We notice that even if we sort the unsorted subarray in the middle, the new array is still in unsorted order:

 [1,2,3] | 6,7,9 | 8,10,23]
---1--------2--------3------
 So we also need to make sure that the maximum value of subarray1(as shown in the above) not larger than the minimum of the subarray2;
 And the maximum value of subarray2 is no larger than the minimum of subarray3. If not, we are aware that the maximum of the subarray1 and the minimum
 of subarray3 should also be included in the unsorted array as the shown subarray2. So we need to change the boundary of our unsorted array. 
 The new boundary 'low' should be the index of the maxmium value of subarray1, and 'high' should be the index of the minimum value of the subarray3. 
 In that way, we can guarantee that we have found the minimum unsorted subarray, sorthing which could give us a completely sorted array.
'''

if __name__ == '__main__':
    arr = [2,1,1,1,1,1]
    print min_unsort_array(arr)
    #nums = [1,8,3,2]
    #print findMax(nums)