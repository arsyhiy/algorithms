# function binary_search(A, n, T) is
#     L := 0
#     R := n − 1
#     while L ≤ R do
#         m := L + floor((R - L) / 2)
#         if A[m] < T then
#             L := m + 1
#         else if A[m] > T then
#             R := m − 1
#         else:
#             return m
#     return unsuccessful
import math
def binary_search(A, t):
    L = 0
    R = len(A) - 1
    while L <= R:
        m = L + math.floor((R - L ) //2) 
        if A[m] == t:
            return m
        elif A[m]< t:
            L = m + 1
        else:
            R = m - 1
    return -1


A = [3, 4, 5, 6, 7, 8, 9]
t = 7
result = binary_search(A, t)
print(result)
