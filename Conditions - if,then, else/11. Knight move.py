pos1_x = int(input("X of current position: "))
pos1_y = int(input("Y of current position: "))

pos2_x = int(input("X of new position: "))
pos2_y = int(input("Y of new position: "))

valid_x = abs(pos1_x - pos2_x)
valid_y = abs(pos1_y - pos2_y)

if valid_x == 1 and valid_y == 2 or valid_x == 2 and valid_y == 1:
    print('YES')
else:
    print('NO')
