""" Given a number X, find the smallest prime number which is grater than X. """

def nextprime(a):
    while True:
        if isprime(a):
            return a
        else:
            a+=1
def isprime(x):
    if x<=1:
        return False
    for i in range (2,x):
        if x%i==0:
            return False
    return True
x=int(input("Enter x: "))
r=nextprime(x+1)
print(r)
