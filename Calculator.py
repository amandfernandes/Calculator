#Calculadora Simple

def calculate():
    while True:
        try:
          num = float(input("Enter a number: "))
        except ValueError:
          print("Invalid input. Please enter a valid number.")
          continue

        if num is None:
            break
        else:
            while True:
                operator = input("Enter your operator: ")
                if operator.lower() in ["+", "-", "*", "/"]:
                  ndnum = float(input("Enter your next number: "))
                  num = operation(num,operator,ndnum)
                  print(num)
                elif operator.lower() == "x" or operator == "":
                  break
                else:
                  print("Invalid operator")
                  break

def operation(a, o,b):
    match o:
        case "+":
            print('{} + {} ='.format(a,b))
            return a + b
        case "-":
            print('{} - {} ='.format(a,b))
            return a - b
        case "*":
            print('{} * {} ='.format(a,b))
            return a * b
        case "/":
            print('{} / {} ='.format(a,b))
            if b == 0:
              print("Can't divide by 0 (Press enter to restart)! ")
            else:
              return a / b

calculate()
    