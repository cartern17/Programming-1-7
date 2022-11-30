def main():
  eggs = int(input("Enter the total number of eggs: "))
  dozens = eggs // 12
  remainder = eggs % 12
  price = 0.0
  cost = 0.0

  if dozens <= 3:
    cost == 0.50
  elif dozens <= 5 and dozens >= 4:
    cost == 0.45
  elif dozens <= 10 and dozens >= 6:
    cost == 0.40
  elif dozens >= 11:
    cost == 0.35
  
    
  
  

  pass


if __name__ == "__main__":
  main()