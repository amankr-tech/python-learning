# #day02_password_checker.py
#     Define a function evaluate_password(password) that checks 4 security rules:
    # Rule 1: Password length is at least 8 characters (len(password) >= 8).
    # Rule 2: Contains at least one uppercase letter (A–Z).
    # Rule 3: Contains at least one lowercase letter (a–z).
    # Rule 4: Contains at least one digit (0–9) or special character from !@#$%^&*

        # 4 rules met  "Strong" 
        # 2 or 3 rules met "Medium"
        # 0 or 1 rule met "Weak"

def evaluate_password(password: str) -> tuple[str, list[str]]:
  has_length = len(password) >= 8
  has_upper = False
  has_lower = False
  has_digit_or_symbol = False

  for char in password:
    if char.isupper():
      has_upper = True
    elif char.islower():
      has_lower = True
    elif char.isdigit() or char in "!@#$%^&*":
      has_digit_or_symbol = True

  score = has_length + has_upper + has_lower + has_digit_or_symbol

  if score == 4:
    strength = "Strong"
  elif score >= 2:
    strength = "Medium"
  else:
    strength = "Weak"

  missing = []
  if not has_length:
    missing.append("at least 8 characters")
  if not has_upper:
    missing.append("uppercase letter")
  if not has_lower:
    missing.append("lowercase letter")
  if not has_digit_or_symbol:
    missing.append("digit or special symbol")

  return strength, missing


password = input("Enter a password to check: ")
strength, missing_rules = evaluate_password(password)

print(f"Password Strength: {strength}")
if missing_rules:
  print(f"Missing: {', '.join(missing_rules)}")