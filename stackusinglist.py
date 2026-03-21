stack=[]
while(True):
    print("\n1. Push | 2. Pop | 3. Peek | 4. Display | 5. Check Empty | 6. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        ele=int(input("Enter Element to Push:"))
        stack.append(ele)
        print("Pushed:",ele)
    elif choice==2:
        if len(stack) == 0:
            print("Stack Underflow! No element to pop.")
        else:
            popele=stack.pop()
            print("Popped element:",popele)
    elif choice==3:
         if len(stack) == 0:
            print("Stack Underflow! No element to pop.")
         else:
            print("Peek element:",stack[len(stack)-1])
    elif choice==4:
        print("Stack:",stack)
    elif choice==5:
        if(len(stack)==0):
            print("Empty Stack")
        else:
            print("Stack is not empty")
    elif choice==6:
        print("Exiting program...")
        break
    else:
        print("Invalid Choice!")


    
