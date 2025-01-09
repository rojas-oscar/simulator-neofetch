import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
from modules.colors import RESET, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BOLD




def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return (f"{RED}Error! Division by zero.{RESET}")
  return x / y

def power(x, y):
  return math.pow(x, y)

def sqrt(x):
  return math.sqrt(x)

def calculator():
  print(f"{YELLOW}Welcome to the terminal calculator!{RESET}")
  print(f"{BOLD}Select operation:{BOLD}")
  print(f"{RED}1. Add{RESET}")
  print(f"{GREEN}2. Subtract{RESET}")
  print(f"{BLUE}3. Multiply{RESET}")
  print(f"{MAGENTA}4. Divide{RESET}")
  print(f"{CYAN}5. Power{RESET}")
  print(f"{RED}6. Square Root{RESET}")
  
  while True:
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice in ['1', '2', '3', '4', '5']:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
        print(f"{BLUE}{num1} + {num2} = {add(num1, num2)}{RESET}")
      elif choice == '2':
        print(f"{BLUE}{num1} - {num2} = {subtract(num1, num2)}{RESET}")
      elif choice == '3':
        print(f"{BLUE}{num1} * {num2} = {multiply(num1, num2)}{RESET}")
      elif choice == '4':
        print(f"{BLUE}{num1} / {num2} = {divide(num1, num2)}{RESET}")
      elif choice == '5':
        print(f"{BLUE}{num1} ^ {num2} = {power(num1, num2)}{RESET}")
    
    elif choice == '6':
      num = float(input("Enter number: "))
      print(f"{BLUE}Square root of {num} = {sqrt(num)}{RESET}")
    
    else:
      print(f"{RED}Invalid input{RESET}")
    
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
      break

if __name__ == "__main__":
  calculator()