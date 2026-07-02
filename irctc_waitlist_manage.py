n1 = int(input("Enter size of first waitlist: "))
list1 = list(map(int, input("Enter first sorted waitlist: ").split()))

n2 = int(input("Enter size of second waitlist: "))
list2 = list(map(int, input("Enter second sorted waitlist: ").split()))

merged = []

i = 0
j = 0

while i < n1 and j < n2:
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

# Add remaining elements
while i < n1:
    merged.append(list1[i])
    i += 1

while j < n2:
    merged.append(list2[j])
    j += 1

print("Merged Waitlist:")
print(merged)