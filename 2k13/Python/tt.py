a = [5, 1, 8, 9, 7, 2, 3, 11, 20, 15]
k = 10
min = a[9]
index = len(a)-1
for i in range(len(a)-2, k-2, -1):
    print(a[i])
    if a[i] < min:
        min = a[i]
        index = i
    else:
        index = i+1
print(index+1)
