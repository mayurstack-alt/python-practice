def add_product():
    productId=str(input("Enter Product ID:"))
    productName=str(input("Enter Product Name:"))
    stockQuantity=int(input("Enter Quantity:"))
    price=int(input("Enter Price:"))
    with open("inventory.txt","a") as f:
        f.write(productId + " " + productName + " " + str(stockQuantity) + " " + str(price) + "\n")
    print("Record added Sucessfully")

def view_inventory():
    print("Inventory Products")
    print("-"*25)
    with open("inventory.txt","r") as f:
        content=f.read()
        if not content:
            print("No records Found")
        else:
            print(content)

def search_product():
    pId=str(input("Enter Product Id:"))
    found=False
    with open("inventory.txt","r") as f:
        for line in f:
            data=line.strip().split()
            if(pId==data[0]):
                print("Product Found")
                print(line)
                found=True
                break
    if not found:
        print("Product not Found")
            

def update_stock():
    pId = input("Enter Product ID:")
    newQuantity = input("Enter New Stock Quantity:")
    updated = False
    lines = []
    with open("inventory.txt", "r") as f:
        for line in f:
            data = line.strip().split()
            if pId == data[0]:
                data[2] = newQuantity
                updated = True
            lines.append(" ".join(data) + "\n")
    with open("inventory.txt", "w") as f:
        f.writelines(lines)
    if updated:
        print("Stock updated successfully")
    else:
        print("Product not Found")    

while(1):
    print("1.Add Product\n2.View Inventory\n3.Search Product\n4.Update Stock\n5.Exit")
    choice=int(input("Enter choice:"))
    if(choice==1):
        add_product()
    elif(choice==2):
        view_inventory()
    elif(choice==3):
        search_product()
    elif(choice==4):
        update_stock()
    elif(choice==5):
        print("Terminating program..")
        break
    else:
        print("Invalid Choice")


