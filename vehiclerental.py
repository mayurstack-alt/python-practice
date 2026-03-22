from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,regNo,brand,rate):
        self.__regNo=regNo
        self.__brand=brand
        self.__rate=0.0
        self.check_rate(rate)

    def get_regNo(self):
        return self.__regNo
    
    def get_brand(self):
        return self.__brand
    
    def get_rate(self):
        return self.__rate
    
    def check_rate(self,rate):
        if rate > 0:
            self.__rate=rate
        else:
            print("Invalid Amount! amount must be positive")

    @abstractmethod
    def calculate_rental_cost(self,days):
        pass

    def display(self):
        print("\nVehicle Details")
        print("Registration Number:",self.__regNo)
        print("Brand:",self.__brand)
        print("Rate per day:",self.__rate)

class Car(Vehicle):

    def __init__(self, regNo, brand, rate,doors):
        super().__init__(regNo, brand, rate)
        self.__doors=doors

    def calculate_rental_cost(self,days):
        if days > 0:
            return self.get_rate() * days
        else:
            print("Invalid Days!")

    def display(self):
        super().display()
        print("Doors:",self.__doors)
        print("Type:CAR\n")

class Bike(Vehicle):
    def __init__(self, regNo, brand, rate,engine_cc):
        super().__init__(regNo, brand, rate)
        self.__engine_cc= engine_cc

    def calculate_rental_cost(self, days):
        if days <= 0:
            print("Invalid Days!")
            return 0
        else:
            cost=self.get_rate()*days
            if self.__engine_cc > 500:
                cost+=cost*0.10
            return cost
    
    def display(self):
        super().display()
        print("Engine CC:",self.__engine_cc)
        print("Type:BIKE\n")

vehicles={}

while(True):
    print("\n1.Add Vehicle\n2.Display All Vehicles\n3.Calculate Rental Cost\n4.Delete Vehicle\n5.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        vtype=input("Enter Vehicle Type (CAR/BIKE):").upper()
        regNo=input("Enter Reg No:")
        brand=input("Enter Brand:")
        rate=float(input("Enter Rate per day:"))

        if vtype=="CAR":
            doors=int(input("Enter Doors:"))
            vehicles[regNo]=Car(regNo,brand,rate,doors)
            print("Added successfully")
        
        elif vtype=="BIKE":
            engine_cc=int(input("Enter Engine CC:"))
            vehicles[regNo]=Bike(regNo,brand,rate,engine_cc)
            print("Added successfully")
        
        else:
            print("Invalid Vehicle Type")
    
    elif choice==2:
        if(len(vehicles)==0):
            print("No Vehicles available")
        else:
            for v in vehicles.values():
                v.display()

    elif choice==3:
        regNo=input("Enter Reg No:")
        if regNo in vehicles:
            days=int(input("Enter Days:"))
            cost=vehicles[regNo].calculate_rental_cost(days)
            print("Rental Cost: ",cost)
        else:
            print("Vehicle not found")
    
    elif choice==4:
        regNo=input("Enter Reg No:")
        if regNo in vehicles:
            del vehicles[regNo]
            print(f"Vehicle {regNo} deleted successfully.")
        else:
            print("Vehicle not found")
    
    elif choice==5:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice")


