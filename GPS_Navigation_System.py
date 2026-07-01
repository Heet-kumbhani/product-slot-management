back_stack = []
forward_stack = []
current = "Home"

def Menu():
    print("\n--- GPS Navigation System ---")
    print("1. Visit New Place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Display")
    print("5. Exit")

def visit(place):
    global current
    
    back_stack.append(current)
    current = place
    forward_stack.clear()
    
    print("Currunt Location", current)

def back():
    global current
    
    if not back_stack:
        print("No previous location.")
        return
    
    forward_stack.append(current)
    current = back_stack.pop()
    
    print("Currunt Location: ",current)

def forward():
    global current

    if not forward_stack:
        print("No forward location.")
        return

    back_stack.append(current)
    current = forward_stack.pop()

    print("Current Location:", current)
    
def display():
    print("\nCurrent Location :", current)
    print("Back Stack       :", back_stack)
    print("Forward Stack    :", forward_stack)

while True:
    Menu()
    ch = eval(input("Enter your choice: "))
    if ch == 1:
        place = input("Enter Place Name: ")
        visit(place)

    elif ch == 2:
        back()

    elif ch == 3:
        forward()

    elif ch == 4:
        display()

    elif ch== 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")