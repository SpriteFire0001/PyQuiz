Finished = False
attempts = 3
num1 = 0
num2 = 0

#Function which allows to user to find the mean of a number.
def average(operator):
  averages = []
  total = 0
  count = int(input("How many numbers do you want to average?"))
  for item_number in range(count):
    item = int(input("What is the " + str(item_number + 1) + " number to average? "))
    averages.append(item)
    total = total + item
  result = total / count
  print("The average of your figures is " + str(result))

#Function which takes the operator from the main function.
def calfunction(operator):
  num1 = int(input("What is the first number?"))
  num2 = int(input("What is the second number?"))
  if operator == "+":
    print(num1 + num2)
  elif operator == "-":
    print(num1 - num2)
  elif operator == "*":
    print(num1 * num2)
  elif operator == "/":
    print(num1 / num2)


Username = input("What is your name?")

#Main function
while Finished == False:
    operator = input("Okay, " + Username + ", input an operator which could be: +, -, *, /. You can say end to terminate the application. Alternatively, you can type mean to calculate the average value of a collection of numerical values.")
    if(operator == "+" or operator == "-" or operator == "*" or operator == "/"):
      calfunction(operator)
    
    elif operator == "end":
      print("Farewell!")
      Finished = True
      
    elif operator == "mean":
      average(operator)

    else:
      print("I did not comprehend that.")
      attempts = attempts - 1
    if(attempts == 0 or attempts <= 0):
      Finished = True

print("Software Terminated")
