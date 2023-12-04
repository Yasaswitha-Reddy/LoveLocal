n = 5
arr = [[1], [1,1]]
for i in range(n-2):
    temp = [1]
    print(arr)
    for j in range(len(arr[-1])-1):
        temp.append(arr[-1][j] + arr[-1][j+1])
    temp.append(1)
    arr.append(temp)
print(arr)