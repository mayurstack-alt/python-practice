def count_characters(password):
    uppercount=0
    lowercount=0
    digitcount=0
    specialcount=0
    for i in password:
        if(i.isupper()):
            uppercount=uppercount+1
        elif(i.islower()):
            lowercount=lowercount+1
        elif(i.isdigit()):
            digitcount=digitcount+1
        else:
            specialcount=specialcount+1
    return uppercount,lowercount,digitcount,specialcount

password=str(input("Enter string:"))
def is_password_valid(password):
    uppercount,lowercount,digitcount,specialcount=count_characters(password)
    if((len(password)>=8) and (uppercount>=2) and (lowercount>=1) and (specialcount>=1)):
        print("Password Valid")
    else:
        print("Password Invalid")
    print("Uppercase letters:",uppercount)
    print("Lowercase letters:",lowercount)
    print("Digits:",digitcount)
    print("Special:",specialcount)

is_password_valid(password)





