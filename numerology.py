n=int(input("Enter number:"))

while(n>=10):
    sum=0
    while(n>0):
        num=n%10
        sum=sum+num
        n=n//10
    n=sum 
print("Digital root:",n)