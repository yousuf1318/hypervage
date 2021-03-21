def findDub(arr, n):
    mp = {i: 0 for i in arr}
    for i in range(n):

        if mp[arr[i]] == 0:
            print(arr[i], end=" ")
            mp[arr[i]] = 1


arr = [1, 2, 5, 1, 7, 2, 4, 2]
n = len(arr)
findDub(arr, n)
