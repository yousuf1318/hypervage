
# pos = -1
# def binary(list, n):
#     l = 0
#     u = len(list)-1
#     while l <= u:
#         mid = (l+u) // 2
#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1;
#             else:
#                 u = mid-1;
#     return False
# list = [4,7,8,12,45,99,102,702,10987,56666]
# n = 12
# if binary(list, n):
#     print("Found at ",pos+1)
# else:
#     print("Not Found")



# def revlist(A,start,end):
#     while start<end:
#         A[start],A[end]=A[end],A[start]
#         start+=1
#         end-=1

# A=[1,2,3,4]
# # print(A)
# revlist(A,0,3)
# print(A)





def issorted(arr):
    n=len(arr)
    if n==1 or n==0:
        return True

    return arr[0]<=arr[1] and issorted(arr[1:])

arr=[20, 22, 23, 45, 78, 88]
if issorted(arr):
    print("yes")
else:
    print("no")