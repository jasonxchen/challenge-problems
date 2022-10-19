# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# https://leetcode.com/submissions/detail/825659514/

def peakIndexInMountainArray(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            start = mid
        else:
                end = mid

print(peakIndexInMountainArray([0,1,4,7,8,10,5,3,2]))    # expect 5
