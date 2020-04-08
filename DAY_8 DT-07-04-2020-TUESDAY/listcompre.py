mylist=[num for num in range(0,100)]
print(mylist)

mylist_1=[num*3 for num in range(0,50)]
print(mylist_1)

mylist_2 = [char for char in 'ALPHANUMERO']
print(mylist_2)

mylist_3 = [num%2 !=0 for num in range(0,100)]
#print(range)
print(mylist_3)

mylist_4 = [num *2 for num in range(0,100) if num %2 == 0]
print(mylist_4)

mylist_5 = [num *2 for num in range(0,100) if num %2 != 0]
print(mylist_5)

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [ letter for letter in 'human' ]
print( h_letters)

letters = list(map(lambda x: x, 'human'))
print(letters)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)


