inventory={}
def add_item():
    itemId=str(input("Enter Item ID:"))
    item_name=str(input("Enter Item Name:"))
    quantity=int(input("Enter Quantity:"))
    price=float(input("Enter Price:"))
    inventory[itemId]=[item_name,quantity,price]
    print("Item added successfully")

def update_quantity():
    itemId=str(input("Enter Item Id to be updated: "))
    if itemId in inventory:
            newQuantity=int(input("Enter the new Quantity:"))
            inventory[itemId][1]=newQuantity
            print("Item updated Successfully")
    else:
        print("Item not found")

def search_item():
    itemId=str(input("Enter Item Id to search:"))
    if itemId in inventory.keys():
        print(inventory[itemId])
    else:
        print("Item Id does not Exist")
    

def display_item():
    if not inventory:
        print("Inventory is empty.")
        return

    id_header = "Item ID"
    name_header = "Name"
    qty_header = "Quantity"
    price_header = "Price"

    id_width = max(len(id_header), max((len(str(k)) for k in inventory.keys())))
    name_width = max(len(name_header), max((len(str(v[0])) for v in inventory.values())))
    qty_width = max(len(qty_header), max((len(str(v[1])) for v in inventory.values())))
    price_width = max(len(price_header), max((len(f"{v[2]:.2f}") for v in inventory.values())))

    header = f"{id_header:<{id_width}}  {name_header:<{name_width}}  {qty_header:>{qty_width}}  {price_header:>{price_width}}"
    sep = "-" * len(header)
    print(header)
    print(sep)

    for k, v in inventory.items():
        print(f"{k:<{id_width}}  {v[0]:<{name_width}}  {v[1]:>{qty_width}}  {v[2]:>{price_width}.2f}")

def total_inventory_value():
    total_value=0
    for k in inventory.values():
        total_value+=k[1]*k[2]
    print("Total Inventory Values:",total_value)
    

def low_stock_items():
    for v in inventory.values():
        if(v[1]<5):
            print("Low Stock Items-",v[0])
        else:
            print("No Low Stock Items")

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Search by Item ID")
    print("4. Display All Items")
    print("5. Total Inventory Value")
    print("6. Low Stock Items")
    print("7. Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        add_item()
    elif choice=="2":
        update_quantity()
    elif choice=="3":
        search_item()
    elif choice=="4":
        display_item()
    elif choice=="5":
        total_inventory_value()
    elif choice=="6":
        low_stock_items()
    elif choice=="7":
        print("Exiting System.")
        break
    else:
        print("Invalid choice.Try again.")
