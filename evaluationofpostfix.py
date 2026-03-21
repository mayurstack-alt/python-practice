expression=str(input("Enter postfix expression:"))
def evaluate_postfix(exp):
    stack=[]
    for i in exp:
            if i.isdigit():
                stack.append(int(i))
            elif i in "+-*/":
                res2=stack.pop()
                res1=stack.pop()
                if i=="+":
                    stack.append(res1+res2)
                elif i=="/":   
                    stack.append(res1//res2)
                elif i=="-":
                    stack.append(res1-res2)
                elif i=="*":
                    stack.append(res1*res2)
    return stack[0]

result=evaluate_postfix(expression)
print("Result:",result)