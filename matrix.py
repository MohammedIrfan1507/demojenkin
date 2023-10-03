r=int(input("Enter the number of rows : "))
c=int(input("Enter the number of columns : "))
matrix=[]
print("Enter the number row wise :")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
row=0
col=0
while row <r and col<c:
    for i in range(col,c):
        print(matrix[row][i],end=" ")
    row +=1
    for i in range(row,r):
        print(matrix[i][c-1],end=" ")
    c-=1
    for i in range(c-1,(col-1),-1):
        print(matrix[r-1][i],end=" ")
    r-=1
    for i in range(r-1,(row-1),-1):
        print(matrix[i][col],end=" ")
    col+=1








