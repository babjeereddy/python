arr = [5, 3, 8, 4, 2]
target = 4

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break
