from itertools import combinations

arr = [3, 34, 4, 12, 5, 2]
target = 7

found = False
for r in range(1, len(arr)+1):
    for subset in combinations(arr, r):
    
        if sum(subset) == target:
            print("Subset found:", subset)
            found = True
            break
    if found:
        break