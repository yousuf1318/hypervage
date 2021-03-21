arr = [2, 3, 6, 8, 9, 10] 
k=9
arr1 = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==k and arr[i] not in arr1:
            print([arr[i], arr[j]])
            arr1.append(arr[i])
            arr1.append(arr[j])