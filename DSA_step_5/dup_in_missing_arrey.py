def printDuplicates(arr, size):
    print("The Duplicates elements are: ")
    for i in range(0, size):
 
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)
printDuplicates(arr, arr_size)
