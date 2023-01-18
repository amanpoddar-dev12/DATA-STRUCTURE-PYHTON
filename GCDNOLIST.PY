def gcd(num1,num2):
    cf=[]
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            common=i
    return common
result=gcd(12,24)
print(result)