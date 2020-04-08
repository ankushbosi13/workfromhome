# age=int(input("enter age"))
# print(age)

# #print(1+true)
# while True:
#             try:
#                 age=int(input("enter the age "))
#                 print(age)
#             except:
#                 print("enter the number")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#     f.close()

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")


