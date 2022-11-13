## code 2

hist = list()
def num_add(num1,num2):# addition function
    num1 = float(num1)
    num2=float(num2)
    add_val = num1+num2
    print(f'{num1} + {num2} = {add_val}')
    hist.append(f'{num1} + {num2} = {add_val}')
    return add_val

def num_sub(num1,num2):# substracion function
    num1 = float(num1)
    num2=float(num2)
    sub_val = num1-num2
    print(f'{num1} - {num2} = {sub_val}')
    hist.append(f'{num1} - {num2} = {sub_val}')

    return sub_val

def num_div(num1,num2):# division function
  num1 = float(num1)
  num2=float(num2)
  if num2==0:
    print("float division by zero")
    print(num1,"/ 0.0 = None")
    hist.append(f'{num1} / 0.0 = None')

  if num2!=0:
    div_val = num1/num2
    print(f'{num1} / {num2} = {div_val}')
    hist.append(f'{num1} / {num2} = {div_val}')

def num_mul(num1,num2):# multipication function
  num1 = float(num1)
  num2=float(num2)
  mul_val = num1*num2
  print(f'{num1} * {num2} = {mul_val}')
  hist.append(f'{num1} * {num2} = {mul_val}')
  return mul_val

def num_pow(num1,num2):# power function
    num1 = float(num1)
    num2=float(num2)
    pow_val = num1**num2
    print(f'{num1} ^ {num2} = {pow_val}')
    hist.append(f'{num1} ^ {num2} = {pow_val}')
    return pow_val

def terminate(): # terminating function
  print("Done. Terminating")

def history():  
  # gives previous operations
  if len(hist) == 0:
    print('No past calculations to show')
  else:
    for i in hist:
      print(i)
  
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(choice == "+"):
    num1 = input("Enter first number: ")
    print(num1)
    if ("$" in num1):
      continue 
    if num1=="#":
      terminate()
      break
      
    num2 = input("Enter second number: ")
    print(num2)
    if ("$" in num2):
      continue
    if num2=="#":
      terminate()
      break

    num_add(num1,num2)


  if choice == "-":
    num1 = input("Enter first number: ")
    print(num1)
    if ("$" in num1):
      continue 
    if num1=="#":
      terminate()
      break

    num2 = input("Enter second number: ")
    print(num2)
    if ("$" in num2):
      continue 
    if num2=="#":
      terminate()
      break

    num_sub(num1,num2)

  if choice == "/":
    num1 = input("Enter first number: ")
    print(num1)
    if ("$" in num1):
      continue 
    if num1=="#":
      terminate()
      break

    num2 = input("Enter second number: ")
    print(num2)
    if ("$" in num2):
      continue

    if num2=="#":
      terminate()
      break

    num_div(num1,num2)

  if choice == "*":
    num1 = input("Enter first number: ")
    print(num1)
    if ("$" in num1):
      continue
    if num1=="#":
      terminate()
      break
 
    num2 = input("Enter second number: ")
    print(num2)
    if ("$" in num2):
      continue 
    if num2=="#":
      terminate()
      break
 
    num_mul(num1,num2)

  if choice == "^":
    num1 = input("Enter first number: ")
    print(num1)
    if ("$" in num1):
      continue 
    if num1=="#":
      terminate()
      break

    num2 = input("Enter second number: ")
    print(num2)
    if ("$" in num2):
      continue
    if num2=="#":
      terminate() 
      break
    num_pow(num1,num2)

  if choice == '?':
    history()

  if choice=="#":
    terminate()
    break