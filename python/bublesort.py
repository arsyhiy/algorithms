# procedure bubbleSort(A : list of sortable items)
#     n := length(A)
#     repeat
#         swapped := false
#         for i := 1 to n-1 inclusive do
#             { if this pair is out of order }
#             if A[i-1] > A[i] then
#                 { swap them and remember something changed }
#                 swap(A[i-1], A[i])
#                 swapped := true
#             end if
#         end for
#     until not swapped
# end procedure
from randomNumberGenerator import random_list
def buble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swapped = False
        for i in range(i):
            if arr[i] > arr[i + 1]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
               swapped = True
        if not swapped:
            break

arr = random_list()
print("unsorted list \n", arr)
print("")
buble_sort(arr)
print("sorted list \n", arr)
