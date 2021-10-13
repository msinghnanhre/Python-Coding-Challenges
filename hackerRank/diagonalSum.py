arr = [[11,2,4], [4,5,6], [10,8,-12]]

def diagonalDifference(arr):
    count = 0
    sum1 = 0
    sum2=0

    while(count < len(arr)):
        sum1+=arr[count][count]
        sum2+=arr[count][len(arr)-1-count]
        count += 1
    
    return abs(sum1-sum2)

print(diagonalDifference(arr))