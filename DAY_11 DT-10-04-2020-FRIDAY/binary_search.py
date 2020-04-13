pos = 1

def search(arr,n):
    l = 0
    u = len(arr)-1
    while l <= u:
        mid = (l+u)//2
        if arr[mid] == n:
            globals()['pos'] = mid
            return pos+1
        else:
            if arr[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
n = int(input('enter the value: '))
position = search(arr,n)
if position < 0:
    print('not found')
else:
    print('found at', position)