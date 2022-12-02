def main():
  eggs = int(input("Enter the total number of eggs: "))
  dozens = eggs // 12
  remainder = eggs % 12
  cost = 0.0

  if dozens <= 3:
    cost = 0.50
  elif dozens <= 5 and dozens >= 4:
    cost = 0.45
  elif dozens <= 10 and dozens >= 6:
    cost = 0.40
  elif dozens >= 11:
    cost = 0.35


  total = cost * dozens + remainder * (cost / 12.0)

  print("The bill is equal to: $", round(total, 2)



if __name__ == "__main__":
  main()