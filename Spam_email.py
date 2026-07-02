n = int(input("Enter number of sender IDs: "))

blacklist = []

print("Enter blacklisted sender IDs:")
for i in range(n):
    blacklist.append(input())

sender = input("Enter incoming sender ID: ")

found = False

for i in range(n):
    if blacklist[i] == sender:
        found = True
        break
if found:
    print("Spam Detected!")
else:
    print("Safe Email.")