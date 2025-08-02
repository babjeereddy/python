def kthmax(lst,n):
    sort =sorted(lst,reverse=True)
    return sort[n-1]

print(kthmax([2,20,30,1],3))

import heapq
def kth_max(arr,k):
    return heapq.nlargest(k,arr)[-1]
print( kth_max([10,20,4,30],3))