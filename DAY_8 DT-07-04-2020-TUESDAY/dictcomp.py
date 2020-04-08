my_dict = {'a_key':12,'b_key':13,'c_key':2 }

alpha = {key:value*2 for key,value in my_dict.items()}
print(alpha)

alpha = {key:value*2 for key,value in my_dict.items() if value%2==0}
print(alpha)

alpha = {key:value*2 for key,value in my_dict.items() if value%2!=0}
print(alpha)

numero = {num:num**5 for num in [1,2,3,4,5]}
print(numero)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)



