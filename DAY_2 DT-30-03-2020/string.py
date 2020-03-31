print("hi")

#functions

print(len("alpha"))

name = "alpha_numero"
print("hi " + "welcome to " + name)

#METHODS

print('  I am alone '.strip())                   # 'I am alone' --> Strips all whitespace characters from both ends.
print('On an island'.strip('d'))                 # 'On an islan' --> # Strips all passed characters from both ends.
print('but life is good!'.split())               # ['but', 'life', 'is', 'good!']
print('Help me'.replace('me', 'you'))            # 'Help you' --> Replaces first with second param
print('Need to make fire'.startswith('Need'))    # True
print('and cook rice'.endswith('rice'))          # True
#print('bye bye'.index(2))
print('still there?'.upper())                   # STILL THERE?
print('HELLO?!'.lower())                        # hello?!
print('ok, I am done.'.capitalize())
print('oh hi there'.find('i'))
print('oh hi there'.count('e'))


print((9 + 9) * 10 / 2)

print(((3 + 7) * 10) / 2)

print((5 + 6) * (13 / 3))

print((5 + (2 * 23)) / 2)

print(2 + 4 * 10 // 2)

###################################expressions

a,b,c = 1,2,3

print(a)

print(b)

print(c)

##############################################


counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2
print(f"the value of counter = {counter}")



print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))



name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

selfish = "1234"
#selfish[3] = "s"
selfish = selfish + "8"
selfish = selfish + "s"

print(selfish)

bool(True)
bool(False)

# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

print("the and operator")
print(bool(1) and bool(0))


print("the or operator")
print(bool(1) or bool(0))

python = 'I am PYHTON'

print(python[1:4])
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1])

#lists

my_list=[1,2,3,4,5,'True','false']
print(my_list)
print(len(my_list))
print(my_list.index(2))
print(my_list.count(2))
print(my_list[3])
print(my_list[1:])
print(my_list[:1] )
print(my_list[-1] )
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:3:2])

my_list = my_list* 2
print(my_list)

my_list = my_list + [100]
my_list.append(100)
my_list.extend([100, 200])
my_list.insert(2, '!!!')
' '.join(['Hello','There'])
print(my_list)


basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

print(basket)
print(new_basket)
print(new_basket2)

list_new = [1,2,3].pop()
print(list_new)


list_new=[1,2,3].pop(1)
print(list_new)

list_new=[1,2,3].remove(2)
print(list_new)

list_new=[1,2,3].clear()
print(list_new)

print(1 in [1,2,5,3] )
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))
print(0 in [1,2,5,3] )


print([1,2,5,3].sort())
print([1,2,5,3].sort(reverse=True))
print([1,2,5,3].reverse() )
print(sorted([1,2,5,3]))
print(list(reversed([1,2,5,3])))

new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

