#3 divides 111, 13 divides 111111 etc.. find a number having all one's which is shortest divisible by a given number which has 3 as its last digit.
k=int(input("Enter a number ending in 3:"))
res=0
if k%10==3:
    r=0
    l=0
    while True:
        l+=1
        r=(r*10+1)%k
        if r==0:
            res=l
            break
if isinstance(res,str):
    print(res)
else:
    print(f"The shortest number of all ones divisible by {k} has {res} digits.")
    print(f"The number is: {'1' * res}")
    
