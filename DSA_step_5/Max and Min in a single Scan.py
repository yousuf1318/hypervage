arr = [5,4,3,6,24,2,45,32,89]
max1 = arr[0]
min1 = arr[0]
for i in arr:
    if i > max1:
        max1 = i
    elif i < min1:
        min1 = i
print("The max element is ", max1)
print("The min element is ", min1)