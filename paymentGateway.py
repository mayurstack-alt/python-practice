from abc import ABC,abstractmethod

class Payment(ABC):
    def __init__(self,amount):
        self.__amount=amount
    
    def get_amount(self):
            return self.__amount
    
    @abstractmethod
    def validate_payment(self):
        pass
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount,CardNo):
        super().__init__(amount)
        self.__cardNo=CardNo

    def validate_payment(self):
        if len(self.__cardNo)==16:
           return True
        else:
            print("Invalid Card Number")
            return False
        
    def process_payment(self):
        if self.validate_payment():
            print("Payment Successful.")
        else:
            print("Payment Failed!")
        

class UPIPayment(Payment):
    def __init__(self, amount,UPIId):
        super().__init__(amount)
        self.__UPIID=UPIId

    def validate_payment(self):

        if "@" not in self.__UPIID:
            print("Invalid UPI ID")
            return False
        else:
            return True
        
    def process_payment(self):
        if self.validate_payment():
            print("Payment Successful")
        else:
            print("Payment Failed")

while(True):
    print("\n1.Make Payment\n2.Exit")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        pType=input("Enter Payment Type(Credit Card/UPI):").lower()
        amount=float(input("Enter Amount:"))

        if amount <= 0:
            print("Invalid Amount")
            continue

        if pType=="credit card":
            cardNo=input("Enter Card Number:")
            card=CreditCardPayment(amount,cardNo)
            card.process_payment()

        elif pType=="upi":
            upiId=input("Enter UPI ID:")
            upi=UPIPayment(amount,upiId)
            upi.process_payment()
        else:
            print("Invalid Payment method")
    elif choice==2:
        print("Exiting Program..")
        break
    else:
        print("Invalid Choice")

            
            


    
        
