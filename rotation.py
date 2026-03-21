string=str(input("Enter String:"))
rot_digit=int(input("Enter rotation digit:"))
rot_type=str(input("Enter rotation type(left/right):"))

def rotation(string,rotdigit,rottype):
    if(rottype=="left"):
        newstr=string[rotdigit:]+string[:rotdigit]
    elif(rottype=="right"):
        newstr=string[-rotdigit:]+string[:-rotdigit]
    return newstr

stringRotation=rotation(string,rot_digit,rot_type)
print(stringRotation)