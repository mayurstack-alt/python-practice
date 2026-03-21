password= "admin@123"
i=1
while(i<=3):
    pw=str(input("Enter the Password:"))
    if(pw==password):
        print("Login Sucessful'")
        break
    else:
        i=i+1
        if(i>3):
            print("Account Locked")
            break
