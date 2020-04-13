def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp





arr=[9,3,5,2,8,6,7,1,4]
sort(arr)
n = len(arr)
print(n)
print(arr)
