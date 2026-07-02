n = eval(input("Enter number of student :"))

marks = list(map(int, input().split()))

for i in range(min(3,n)):
  max_ind = i

  for j in range(i + 1, n):
    if marks[j] > marks[max_ind]:
      max_ind = j 
    
    marks[i], marks[max_ind] = marks[max_ind], marks[i]

print("TOp 3 std:")
for i in range(min(3,n)):
  print(marks[i])