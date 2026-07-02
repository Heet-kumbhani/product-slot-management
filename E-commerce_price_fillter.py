n = int(input("Enter number of products: "))

prices = list(map(int, input("Enter sorted prices: ").split()))

target = int(input("Enter target price: "))

low = 0
high = n - 1
answer = -1
while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1
if answer != -1:
    print("First product price >= target is", prices[answer])
    print("Position:", answer + 1)
else:
    print("No product found with price >= target")