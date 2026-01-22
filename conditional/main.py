#number comparison & grading system
score = int(input("enter your score(0-100):"))
# conditional statement
if score>= 90:
  grade = "A+"
elif score>= 75:
  grade = "A"
elif score>= 60:
  grade = "B"
elif score>= 50:
  grade = "C"
else:
  grade = "F"

print(f"your score is {score} , so your grade is {grade}")

num1 =int(input("\nEnter first number to compare:"))
num2 =int(input("\nEnter second number to compare:"))
if num1 > num2 :
 print(f"{num1} is greater than {num2}")
elif num1 < num2:
 print(f"{num1} is smaller than {num2}")
else :
 print(f"{num1} is equal to {num2}")

