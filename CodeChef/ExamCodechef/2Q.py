# source https://www.geeksforgeeks.org/python-program-for-quicksort/ 
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# https://www.geeksforgeeks.org/minimum-difference-max-min-k-size-subsets/
def minDifferenceAmongMaxMin(arr, N, K): 
  
  
    # initialize result by a 
    # big integer number 
    res = 2147483647
  
    # loop over first (N - K) elements 
    # of the array only 
    for i in range((N - K) + 1): 
          
        # get difference between max and min  
        # of current K-sized segment 
        curSeqDiff = arr[i + K - 1] - arr[i] 
        res = min(res, curSeqDiff) 
      
    return res
T = int(input())
for _ in range(T):
    N,K= map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    if K < 2:
        print("0")
    else:
        quickSort(arr, 0, N-1)
        if K == N:
            print(arr[N-1] - arr[0])
        else:
            print(minDifferenceAmongMaxMin(arr, N, K))