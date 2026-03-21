inventory={}
def add_item():
    itemId=str(input("Enter Item ID:"))
    item_name=str(input("Enter Item Name:"))
    quantity=int(input("Enter Quantity:"))
    price=float(input("Enter Price:"))
    if itemId in inventory.keys():
        print("Item already exists")
    else:
        inventory[itemId]=[item_name,quantity,price]
        print("Item added successfully")

def sell_item():
    itemId=str(input("Enter Item ID To Sell:"))
    if itemId in inventory:
        quantity=int(input("Enter Quantity To Sell:"))
        if quantity>inventory[itemId][1]:
            print("Insufficient Stock!")
        else:
            newQuantity=inventory[itemId][1]-quantity
            inventory[itemId][1]=newQuantity
            print(quantity,"items sold. Remaining Stock:",newQuantity)    
    else:
        print("Item Id does not exist!")
    
def display_low_stock_items():
    found=False
    for itemId in inventory:
        if(inventory[itemId][1]<5):
            print("Low Stock Item:",inventory[itemId][0])
            found=True
        
    if(found==False):
        print("No low stock Items")

def calculate_total_inventory_value():
    total_value=0
    for v in inventory.values():
        total_value+= v[1]*v[2]
    print("Total Inventory Value: ",total_value)

def display_all_items():
    if not inventory:
        print("Inventory is empty")
    else:
        print("-----------------------------------------------")
        print("ID | Name | Price | Quantity")
        print("-----------------------------------------------")
        for key,values in inventory.items():
            print(key," |",values[0]," |",values[1]," |",values[2])
        print("-----------------------------------------------")

while(True):
    print("\nINVENTORY MANAGEMENT SYSTEM")
    print("1. Add Item")
    print("2. Sell Item")
    print("3. Display Low Stock Items")
    print("4. Calculate Total Inventory Value")
    print("5. Display All Items")
    print("6. Exit")
    choice=int(input("Enter choice:"))
    if(choice==1):
        add_item()
    elif(choice==2):
        sell_item()
    elif(choice==3):
        display_low_stock_items()
    elif(choice==4):
        calculate_total_inventory_value()
    elif(choice==5):
        display_all_items()
    elif(choice==6):
        print("Exiting Progam...")
        break
    else:
        print("Invalid choice!")