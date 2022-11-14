def main():
  weight = int(input("Enter weight in kilometers: "))
  length = int(input("Enter length in centimeters: "))
  width = int(input("Enter width in centimeters: "))
  height = int(input("Enter height in centimeters: "))

  if width * length * height > 100000 and weight > 27:
    print("Too Big\nToo Heavy")
  elif width * length * height > 100000:
    print("Too Big")
  elif weight > 27:
    print("Too Heavy")
  else:
    print("All Good")

  pass


if __name__ == "__main__":
  main()