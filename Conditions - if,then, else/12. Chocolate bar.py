n = int(input("Length: "))
m = int(input("Width: "))

k = int(input("Squares: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
