my_set = {char for char in "alpha numero"}
print(my_set )

mylist={num for num in range(0,100)}
print(mylist)

mylist_1={num*3 for num in range(0,50)}
print(mylist_1)

mylist_2 = {char for char in 'ALPHANUMERO'}
print(mylist_2)

mylist_3 = {num%2 !=0 for num in range(0,100)}
#print(range)
print(mylist_3)

mylist_4 = {num *2 for num in range(0,100) if num %2 == 0}
print(mylist_4)

mylist_5 = {num *2 for num in range(0,100) if num %2 != 0}
print(mylist_5)


