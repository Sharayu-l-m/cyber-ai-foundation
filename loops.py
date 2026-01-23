# multiplication table
num = int(input("enter a number to see its multiplication tablr:"))

print(f"Multiplication table for {num}:")
for i in range (1,11):
  print(f"{num} x {i} = {num * i}")

print("\nCheck even or odd numbers from 1 to 10:")
for i in range(1,11):
  if i% 2==0:
    print(f"{i} is even")
  else:
    print(f"{i} is odd")
