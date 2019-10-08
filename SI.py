def simple_interest(p,r,t):
    return (p*r*t)/100
p=float(input("enter the principle"))
r=float(input("enter the rate"))
t=int(input("enter the time"))
Si=simple_interest(p,r,t)
print("Simple interest of p={},r={},t={} is ={}".format(p,r,t,Si))