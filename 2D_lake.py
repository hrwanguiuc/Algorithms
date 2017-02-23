
def solution(h, d):
    if not h or not d:
        return 0
    # MAX is the result to return
    MAX = 0
    stack = []
    i = 0 
    L = len(h)

    while i < L:
        area = 0
        if not stack or h[i] <= h[stack[-1]]: # stack.peek()
            stack.append(i) # stack.push_back(i)
            i += 1
        else:
            base = stack.pop() # stack.pop()
            l = 0
            # when stack is empty, find the left boundary
            if not stack:
                l = base
            # when stack is not empty, the top element is the index
            else:
                l = stack[-1] 
            r = i
            height = min(h[l], h[r])
            
            width = 0 # width
            for j in xrange(l, r):
            #for(j=l;j<r;j++):
                width += d[j]
            width += (r-l-1)
            area_to_delete = 0
            for k in xrange(l+1, r):
            # for(k=l+1;k<r;k++)
                area_to_delete += h[k]
            area = height*width - area_to_delete
            MAX = max(MAX, area)
    # special case 
    if MAX == 0 and stack:
        for i in xrange(L-1):
        # for(int i=0;i<L-1,i++)
            temp = min(h[i],h[i+1])*d[i]
            MAX = max(MAX, temp)

    return MAX 



if __name__ == '__main__':
    h = [7,9,5,4,6]
    d = [2,1,5,1]
    print solution(h,d)


