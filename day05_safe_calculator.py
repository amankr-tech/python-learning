# day05_safe_calculator.py


def get_number(prompt: str) -> float:
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid number! Please enter a valid numeric value.")


print("--- Safe Calculator ---")

while True:
  choice = input("\nChoose operation (+, -, *, /) or 'exit': ").strip().lower()

  if choice == "exit":
    print("Calculator closed.")
    break

  if choice not in ("+", "-", "*", "/"):
    print("Invalid operation, please enter +, -, *, /, or 'exit'.")
    continue

  num1 = get_number("Enter first number: ")
  num2 = get_number("Enter second number: ")

  if choice == "+":
    result = num1 + num2
  elif choice == "-":
    result = num1 - num2
  elif choice == "*":
    result = num1 * num2
  elif choice == "/":
    try:
      result = num1 / num2
    except ZeroDivisionError:
      print("Error: Cannot divide by zero.")
      continue

  print(f"Result: {num1} {choice} {num2} = {result:.2f}")