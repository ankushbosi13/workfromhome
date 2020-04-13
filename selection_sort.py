def sort(arr):
    for i in range((len(arr)-1)):
        minpos = i
        for j in range(i,len(arr)):
            if arr[j] > arr[minpos]:
                minpos = j
        temp = arr[i]
        arr[i] = arr[minpos]
        arr[minpos] = temp

arr=[9,3,5,2,8,6,7,1,4]
sort(arr)
n = len(arr)
print(n)
print(arr)
