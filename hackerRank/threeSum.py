def threeSum(arr,target):
    left = 1
    right = len(arr)-1
    for num in range(len(arr)):
        while left < right:
            if(arr[num] + arr[left]+ arr[right] == target):
                return (arr[num], arr[left], arr[right])
            elif (arr[num] + arr[left] + arr[right] < target):
                left += 1
            else:
                right -= 1


print(threeSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15], 14))
