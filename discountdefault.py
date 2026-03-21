def apply_discount(price,discount=5):
    discountedPrice=price-(price*(discount/100))
    return discountedPrice

result=apply_discount(1000,10)
print("Final Price:",result)