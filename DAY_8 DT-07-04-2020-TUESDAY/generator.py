def make_list(num):
    list_1 =[]
    for i in range(num):
        i=i*2
        list_1.append(i)
    return list_1

result = make_list(10)
print(result)
