def CI(p, r, t, n):
    r = r / (n * 100)
    ci = p * ((1 + r) ** round(n * t))
    return ci


p = float(input("Enter :THE INITIAL AMOUNT YOU BORROW OR DEPOSIT"))
r = float(input("Enter:ANNUAL RATE OF INTEREST{as a decimal}"))
t = int(input("Enter:NUMBER OF YEARS THE AMOUNT IS DEPOSITED OR BORROWED FOR"))
n = int(input("Enter:NUMBER OF TIMES THE INTEREST IS COMPOUNDED PER YEAR"))
# A=amount of money accumulated after n years,including interest
print("principal amount:{}\tannual rate:{}\tnumber of yeras:{}\tnumberof times:{} ".format(p, r, t, n))
vari=CI(p, r, t, n)
print(" Amount =",vari )
print("\n\t\t\t\tis that qustion is semi type\t\t\t\t\n")
opti = int(input("select option\n\t1=Yes\n\t2=No"))
if opti==1:
    Ci=vari-p
    print("Compound interest is =",Ci)
elif opti==2:
    print("Compound interest is =", vari)
else:
    print("!!!!------Wrong option------!!!!")


