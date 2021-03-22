
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if ar[j] > ar[j+1]:
               ar[j], ar[j+1] = ar[j+1], ar[j]

ar = [5,4,1,2,3,5,7,2]
# inp1=int(input("Enter the len of arr"))
# emp_err=[]
# for i in range(inp1):
#     ar=int(input("enter the numbers"))
#     emp_err.append(ar)
#     print(ar)

bubbleSort(ar)
print ("Sorted array is:")
for i in range(len(ar)):
   print (ar[i])

