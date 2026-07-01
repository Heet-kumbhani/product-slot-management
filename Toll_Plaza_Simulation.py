SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

def menu():
    print("\n-----Toll Plaza-----")
    print("1. Add vehical.")
    print("2. Remove Vehical.")
    print("3. Display Queue.")
    print("4. Exit")

def isFUll():
    return (rear + 1) % SIZE == front

def isEmpty():
    return front == -1

def add_vehical(vehicle):
    global front, rear
    
    if isFUll():
        print("Toll Plaza is Full! vehicle must wait.")
        return
    if front == -1:
        front = rear = 0
    else:
        rear = (rear + 1) % SIZE
    
    queue[rear] = vehicale
    print(vehicale, "entered the toll plaza.")

def remove_vehicle():
    global front,rear
    
    if isEmpty():
        print("Toll Plaza is Empty!")
        return
    
    print(queue[front], "has crossed the toll.")
    
    if front == rear:
        front = rear =-1
    else:
        front = (front + 1) % SIZE
    
def display():
    if isEmpty():
        print("No vehicle in the queue.")
        return
    
    print("\n vehicles in queue.")
    
    i = front
    
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % SIZE
    print()
    
while True:
    menu();
    ch = eval(input("Enter your choice:"))
  
    if ch == 1:
        vehicale = input("Enter vehicle number:")
        add_vehical(vehicale)
    elif ch == 2:
        remove_vehicle()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Thenk you...")
        break
    else:
        print("wrong choice...")