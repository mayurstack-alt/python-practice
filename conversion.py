def decimalToBinaryConversion(num):
    if(num==0):
        return "0"
    if(num==1):
        return "1"
    else:
        return decimalToBinaryConversion(num//2)+str(num%2)
    
n=int(input("Enter decimal number:"))
convertedNumber=decimalToBinaryConversion(n)
print("Binary representation =",convertedNumber)