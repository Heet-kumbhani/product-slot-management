def binary_search(l, key, low, high):
    if low > high:
      return -1:
    
    mid = high + low // 2
    
    if l[mid] == key:
      return mid
    elif l[mid] > key:
      return binary_search(l, key, low, mid - 1)
    else:
      return binary_search(l, key, mid + 1, high)


l = list(map(int, input("Enter data using space: ").split(" ")))
target = eval(input("Enter number to find :"))
res = binary_search(l, target, 0, len(l)-1)

if res != -1:
  print(target, "is found at",res+1,"position...")
else:
  print("Target not found of any position...")