arr = [2,5,1,10,3,7,6,9,8]

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i =j =k =0

        while i<len(left) and j< len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

mergeSort(arr)
printList(arr)
