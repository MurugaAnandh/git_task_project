#pseudocode
#======================
# Used print statement to print "Hello World!"

#print(Hello World!)

user_name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Added Welcome Comments and age criteria
if age <= 10:
  print(f"Age criteria is not met")
  print(f"Age should be more than 10 to use Github") # Comment Added
else:
  print(f"Welcome to Git {user_name}")
  print(f"Git is Awesome")