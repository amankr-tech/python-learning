# Smart Bill Splitter

total_amount = float(input("Enter your total bill: "))
person_no = int(input("How many people are splitting the bill: "))

if person_no <= 0:
  print("Error: Number of people must be at least 1.")
else:
  tip = 0.0
  tip_query = (
      input("Do you want to add a tip? (yes or no): ").lower().strip()
  )

  if tip_query == "yes":
    tip = float(input("\tThank you for giving a tip.\nHow much tip amount: "))

  each_person = (total_amount + tip) / person_no
  print(f"\n\tEach person has to pay: {each_person:.2f}")
  print("\tThank you for visiting.")