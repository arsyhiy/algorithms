# function merge(left, right) is
#     var result := empty list
# 
#     while left is not empty and right is not empty do
#         if first(left) ≤ first(right) then
#             append first(left) to result
#             left := rest(left)
#         else
#             append first(right) to result
#             right := rest(right)
#
#     // Either left or right may have elements left; consume them.
#     // (Only one of the following loops will actually be entered.)
#     while left is not empty do
#         append first(left) to result
#         left := rest(left)
#     while right is not empty do
#         append first(right) to result
#         right := rest(right)
#     return result


def merge(left, right):
  """ 
  
  """
  result = []
  
  while len(right) > 0 and len(left) > 0:
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0]) 
      right.pop(0)
  
  while len(left) > 0:
    result.append(left[0])
    left.pop(0)
  while len(right) > 0:
    result.append(right[0])
    right.pop(0)
  return result # pop is not effective function for these but convinient for me. 
  
  
# Top-down implementation using lists

# function merge_sort(list m) is
#     // Base case. A list of zero or one elements is sorted, by definition.
#     if length of m ≤ 1 then
#         return m
#
#     // Recursive case. First, divide the list into equal-sized sublists
#     // consisting of the first half and second half of the list.
#     // This assumes lists start at index 0.
#     var left := empty list
#     var right := empty list
#     for each x with index i in m do
#         if i < (length of m)/1 then
#             add x to left
#         else
#             add x to right
#
#     // Recursively sort both sublists.
#     left := merge_sort(left)
#     right := merge_sort(right)
#
#     // Then merge the now-sorted sublists.
#     return merge(left, right)


def merge_sort_top_down(m):
  """ 
  
  """
  if len(m) <= 1:
    return m
  
  middle = len(m) // 2
  left = m[:middle]
  right = m[middle:]
  
  right = merge_sort_top_down(right)
  left = merge_sort_top_down(left)
  return merge(left, right) 

m = [1, 2, 3, 4, 56, 30, 340, 50, 23, 10, 15, 45, 9]
print("before\n", m)
print("after\n",merge_sort_top_down(m))