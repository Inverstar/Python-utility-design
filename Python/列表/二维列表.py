matrix = [[0 for i in range(3)] for i in range(3)]
matrix = [[i+j for i in range(3)] for j in range(3)]
print(matrix)
x = []
for i in range(4):
        x.append([1]*3)
print(x)
x[0][0] = 2
print(x)