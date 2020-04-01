# R=3
# C=3
# mat = [[int(input()) for x in range (C)] for y in range(R)]
# print(mat)


dictioanry = {"a":1,"b":2,"c":3  }
print(dictioanry)

print(dictioanry['a'])
print(dictioanry['c'])

# Creating a Dictionary
Dict = {1: 'alpha', 2: 'numero', 3: 'solutions'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'alpha', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

list_1 = [ {"abc":123,"second" : 234},
           {"efg":12323,"random" : 12},
           ]
print(list_1)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

#tuple form
Dict = dict({1: 'naruto', 2: 'For', 3:'zoho'})
print("\nDictionary with the use of dict(): ")
print(Dict)

#list form
Dict = dict([(1, 'anime'), (2, 'collection')])
print("\nDictionary with each item as a pair: ")
print(Dict)

user = {
        "basket":[1,2,3],
        "age":52
}

user.update({"age":43})
print(user)


print(user.get('age',24))

#printing in the dictionary from
user2= dict(name='john')
print(user2)



