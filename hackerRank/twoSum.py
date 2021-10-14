def twoSum(arr, target):
    left =0 
    right = len(arr) - 1

    while(left < right):
        if(arr[left]+ arr[right] == target):
            return (left,right)
        elif(arr[left]+ arr[right] < target):
            left = left + 1
        else:
            right = right - 1

print(twoSum([1,2,3,4,5,6,7,8,9,12,14,15], 14))