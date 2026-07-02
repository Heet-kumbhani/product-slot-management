
n = eval(input("Enter number of std :"))

std = []

for i in range(n):
    std.append(input())

find  = input("Enter name for search: ")

flag = False

for i in range(n):
    if std[i].lower() == find.lower():
        print(find, "is present at position",i+1)
        flag = True
        break

if not flag:
    print(find, "is absent")