n=int(input("Enter Integer:"))

def perfect(n):
    counter=0
    for i in range(1,n):
        if(n%i==0):
            counter+=i        
    return counter==n

if(perfect(n)):
    print("True")
else:
    print("False")



    