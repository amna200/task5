name = input("Enter your name: ")
age = input("Enter your age: ")
street = input("Enter your street: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

print("\"Name:" + name + "\"")
print("\"Age:" + age + "\"")
print("\"Address:" + street + "," + city + "," + country + "\"")

NewAge = int(age) -5
age1 = str(NewAge)
print("\"Hello " + name + " Your old is " + age1 + " years old, Your address is " +
      street + " , " + city + " , " + country + ".\"")

print(type(name), type(age), type(street), type(city), type(country))

print("\"Hello '" + name + "', How Are You? \"\"\" Your Age Is \"" + age1 + " \"\" " + " + " +
      "And Your Country Is: " + country + "\"")

Q6 = """\"Hello '{Ali}', How Are You? \\
\"\"\" Your Age Is \"{17}\"\"\" + And
 Your City Is: {Gaza}\""""
print(Q6)

