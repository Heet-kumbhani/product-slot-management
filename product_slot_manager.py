l = ["Laptop","Mouse","Keyboard","Headphones",
     "Charger","Camera","Speaker","Watch"]

slot = eval(input("Enter slot numer(1-8): "))
print("product at slot ",slot,":",l[slot-1])


product = input("\nEnter product to find: ")
if product in l:
    print(product, "found at slot", l.index(product)+1)
else:
    print(product, "not fount")
    
slot = eval(input("Enter a slot number for update(1-8): "))
new_product = input("Enter new product :")

if new_product in l:
    print(new_product, "is already in slot.")
else:
    l[slot-1] = new_product
    print(l)

if None in l:
    print("Belt is NOT full")
else:
    print("Belt is full")