x = int(input("Give a number -->> "))
print("The divisors are: ")

for i in range(1, x + 1):
  if (x % i) == 0:
    print(i)