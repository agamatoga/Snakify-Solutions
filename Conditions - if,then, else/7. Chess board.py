pos1_x = int(input("X of current position: "))
pos1_y = int(input("Y of current position: "))

pos2_x = int(input("X of new position: "))
pos2_y = int(input("Y of new position: "))

if (pos1_x + pos2_x + pos1_y + pos2_y) % 2 == 0:
    print("YES")
else:
    print("NO")
