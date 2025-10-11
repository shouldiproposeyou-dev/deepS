#creating vote.py
try:
  age = int(input("enter your age:"))
  if age >=18:
  print("you are eligible to vote.")
else:
  print("ypu are not eligible to vote.")
    expect valuError:
   print("please enter a valid integer for age")
