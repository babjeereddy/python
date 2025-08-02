def copy_list(arr):
    new_list = []
    for item in arr:
        new_list.append(item)
    return new_list
arr=[10,20,30,40]
new_lst =copy_list(arr)
print(new_lst)
