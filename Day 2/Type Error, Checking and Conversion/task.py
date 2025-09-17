print(type("Hello"))
print(type(12123243))
print(type(3.14))
print(type(True))

print(int("123") + int("123"))
print(str(123) + str(123))
print(float(123) + float(123))

name = input("Enter your name: ")
print("Number of letters in your name: " + str(len(name)))

# Another example
print("We need address names length.")
address = input("Please enter your address:\n")
print("Your address length is " + str(len(address)))