def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
result =  linear_search( [10,20,30,40,50],50 )
print(result)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

result=find_max([10,100,20,40])
print(result)