yearInput = int(input("Enter a year: "))

if yearInput % 4 == 0 and (yearInput % 100 != 0 or yearInput % 400 == 0):
    print("LEAP")
else:
    print("COMMON")
