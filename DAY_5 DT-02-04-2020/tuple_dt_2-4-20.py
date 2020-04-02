my_tuple=('pen','paper','rock','paper','sicissor','pencil')

print(len(my_tuple))
print(my_tuple)

#my_tuple[2] = ("fruit")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


empty_tuple = ()
print (empty_tuple)

tup = 'python', 'java'
print(tup)

# Another for doing the same
tup = ('python', 'c++')
print(tup)

tuple1 = (0, 1, 2, 3)
tuple2 = ('alpha', 'numero')
print(tuple1+tuple2)

tuple3 = ('ALPHA _ NUMERO',)*3
print(tuple3)

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
#
# tuple3 = ( 0, 1)
# del tuple3
# #print(tuple3)
#
# # A python program to demonstrate the use of
# # cmp(), max(), min()
#
# tuple1 = ('python', 'geek')
# tuple2 = ('coder', 1)
#
# #if (cmp(tuple1, tuple2) != 0):
#
# 	# cmp() returns 0 if matched, 1 when not tuple1
# 	# is longer and -1 when tuple1 is shoter
# print('Not the same')
# #else:
# #	print('Same')
# print ('Maximum element in tuples 1,2: ' +
# #		str(max(tuple1)) + ',' +
# #		str(max(tuple2)))
# print ('Minimum element in tuples 1,2: ' +
# 	str(min(tuple1)) + ',' + str(min(tuple2)))

my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
print(my_data)

# true
print(22 in my_data)

# false
print(2 in my_data)

# false
print(88 not in my_data)

# true
print(101 not in my_data)

# tuple of fruits
my_tuple = ("Apple", "Orange", "Grapes", "Banana")

# iterating over tuple elements
for fruit in my_tuple:
     print(fruit)

my_tuple = 3, 4.6, "dog"
print(my_tuple)   # Output: 3, 4.6, "dog"

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)




