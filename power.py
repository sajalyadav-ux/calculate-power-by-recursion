def power2(x,n):
    if n==0:
        return 1
    powA=x*power2(x,(n-1))
    return powA
x=int(input("enter the value :"))
n=int(input("enter the value :"))
result=power2(x,n)#print(power2(x,n))
print(result)
