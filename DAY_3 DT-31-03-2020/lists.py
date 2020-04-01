list=["MATRIX"]
print(list)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])


matrix_1 = [[1,2.6,-5],[4,5,-2],[0,-1,9]]
matrix_2 = [[2.9,-4,0],[3.8,5,6],[5,0,9]]

sum = matrix_1 + matrix_2
print(sum)

mul= matrix_1 * 2
print(mul)


A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A)
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column_1 = [];
column_2 = [];
column_3 = [];

for row in A:
  column_1.append(row[0])
  column_2.append(row[1])
  column_3.append(row[2])


print("1st column_1 =", column_1)
print("2nd column_2=", column_2)
print("3rd column_3 =", column_3)

# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

print("result=",result)
for r in result:
   print("result in for loop = ",r)


a = [ [2, 4, 6, 8 ],
	[ 1, 3, 5, 7 ],
	[ 8, 6, 4, 2 ],
	[ 7, 5, 3, 1 ] ]

for i in range(len(a)) :
	for j in range(len(a[i])) :
		print(a[i][j], end=" ")
	print()


m = 4
n = 5

a = [[0 for x in range(n)] for x in range(m)]
print(a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a.append([5, 10, 15, 20, 25])
print(a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[0].extend([12, 14, 16, 18])
print(a)

a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
a[2].reverse()
print(a)

        # import numpy
        #
        # # initializing matrices
        # x = numpy.array([[1, 2], [4, 5]])
        # y = numpy.array([[7, 8], [9, 10]])
        #
        # # using add() to add matrices
        # print ("The element wise addition of matrix is : ")
        # print (numpy.add(x,y))
        #
        # # using subtract() to subtract matrices
        # print ("The element wise subtraction of matrix is : ")
        # print (numpy.subtract(x,y))
        #
        # # using divide() to divide matrices
        # print ("The element wise division of matrix is : ")
        # print (numpy.divide(x,y))
        #

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


matrix = []
print("Enter the entries rowwise:")


for i in range(R):
    a =[]
    for j in range(C):
         a.append(int(input()))
    matrix.append(a)


for i in range(R):
    for j in range(C):
        #print(i)
        print(matrix[i][j], end = " ")
    print()

mat = [[int(input()) for x in range (C)] for y in range(R)]

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

print(friends.sort() + new_friend)
friends.extend(new_friend)
print(sorted(friends))

