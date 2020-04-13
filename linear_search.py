pos = 1

def search(arr,n):
    i = 0
    while i< len(arr):
        if arr[i] == n:
            globals()['pos'] = i
            return pos+1
        i = i+1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
n = int(input('enter the value: '))
position = search(arr,n)
if position < 0:
    print('not found')
else:
    print('found at', position)
