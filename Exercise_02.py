main_number = int(input("Input a number: "))

if (main_number % 2) == 1:
  print("The number is odd")
else:
  print("The number is even")

condition = input("\nDo you want some extra? [Y/n] -->> ")
conditioner1 = condition.upper()

if conditioner1 == "Y":
  if (main_number % 4) == 0:
    print("The number is multiple of 4")
  elif (main_number % 2) == 0:
    print("The number is even")
  else:
    print("The number is odd")
  
  condition = input("\nDo you want some extra? [Y/n] -->> ")
  conditioner2 = condition.upper()

  if conditioner2 == "Y":
    second_number = int(input("Input the number: "))
    check = int(input("Input a divider: "))
    
    if (second_number % check) == 0:
      print(second_number, "is dividing evenly with", check)
    else:
      print(second_number, "isn't dividing evenly with", check)