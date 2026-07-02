# Number of blacklisted sender IDs
n = int(input("Enter number of sender IDs: "))

# Input blacklist
blacklist = []

print("Enter blacklisted sender IDs:")
for i in range(n):
    blacklist.append(input())

# Incoming sender ID
sender = input("Enter incoming sender ID: ")

# Linear Search
found = False

for i in range(n):
    if blacklist[i] == sender:
        found = True
        break

# Display result
if found:
    print("Spam Detected!")
else:
    print("Safe Email.")