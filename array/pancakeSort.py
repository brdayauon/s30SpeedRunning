def pancake_sort(arr):
  def findMaxIndex(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
  
  def flip(arr,k):
    left = 0
    right = k
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1
  
  n = len(arr)
  
  while n > 1:
    #find indx of mx in 0->n
    mxIndex = findMaxIndex(arr,n)
    flip(arr, mxIndex)
    flip(arr, n-1)
    n -= 1
  return arr
    
  
  pass # your code goes here