try:
    balance=float(input("Enter Account Balance:"))
    withdrawAmount=float(input("Enter Withdrawal Amount:"))
    if balance < 0:
        print("Error:Invalid Balance")
    elif withdrawAmount < 0 :
        print("Error:Invalid Withdrawal")
    elif withdrawAmount > balance:
        print("Error:Insufficient Balance")
    else:
        print(f"Transaction Successful.Remaining Balance:{int(balance - withdrawAmount)}")
except ValueError :
    print("Error:Invalid Input")
except Exception as e:
    print("Error:",str(e))