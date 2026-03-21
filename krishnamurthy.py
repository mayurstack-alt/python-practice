
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
def is_krishnamurthy(num):
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        sum=sum+factorial(digit)
        temp=temp//10
    return sum==num

number=int(input("Enter the number:"))
if (is_krishnamurthy(number)):
    print("Krishnamurthy Number")
else:
    print("Not a Krishnamurthy Number")    
