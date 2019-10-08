def facto(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * facto(i - 1)


i = int(input("Enter the number"))
print("given number {}! factorial is {}".format(i, facto(i)))
