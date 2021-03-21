arr = [1,6,2,7,4,8,4,4]
k=9
for i in arr:
    for j in range(1, len(arr)-1):
        if i+arr[j]==k and i != arr[j]:
            print([i, arr[j]])