# Dictionary
# Stores data values in Key : Value pairs
# They are unordered
# They are mutuable
# Dont allow duplicates
# We can have nested dictionary

# dict = {
#     "Name" : "Preyansh",
#     "Age" : "21",
#     "temp" : "temp",
#     "Name" : "temp", # Here Name is changed from Preyansh to temp
#     "Name" : "temp" # Here duplicate value is not added
# }

# print(dict)
# print(type(dict))
# print(dict["Name"])
# # print(dict["name"]) # Invalid
# dict["Name"] = "1" # Replace value
# print(dict)
# dict["temp12"] = 123
# print(dict)
# # We can create a null dict
# te = {}
# print(te)
# print(type(te))








# # Dictionary Methods
# dict = {
#     "Name" : "Preyansh",
#     "Age" : "21",
#     "temp" : "temp"
# }

# print(dict.keys()) # Returns all keys
# print(list(dict.keys()))
# print(dict.values()) # Returns all values
# print(dict.items()) # Return key value pairs
# print(dict.get("Preyansh")) # Returns value according to key and return None if does not exist
# dict.update({"Name":"Temp","Surname" : "Jain"}) # Updates dictionary with set of key value pairs
# print(dict)








# Set
# Collection of unordered items
# Each element in set must be unique and immutable
# Set is mutable

# s = {1,2,3,4,5}
# print(s) 
# print(type(s))

# t = set()
# print(t)
# print(type(t)) # This is set
# a = {}
# print(a)
# print(type(a)) # This is dictionary







# # Set Methods
# s = {1,2,3,4}
# s.add(7) # adds an element
# print(s)
# s.remove(2) # removes an element
# print(s)
# s.pop() # removes a random value
# print(s)
# s.clear() # removes all elements
# print(s)
# s1 = {1,2,3}
# s2 = {1,3,5,6}
# s3 = s1.union(s2)
# s4 = s1.intersection(s2)
# print(s1)
# print(s2)
# print(s3)
# print(s4)










# Write a program to take marks of 3 subjects and store in dict
# initially the dict is empty and then add one by one 
# use subject name as key and marks as value
# dict = {}
# subject = input("Enter subject name : ")
# marks = int(input("Enter " + subject + " marks : "))
# dict.update({subject : marks})
# subject = input("Enter subject name : ")
# marks = int(input("Enter " + subject + " marks : "))
# dict.update({subject : marks})
# subject = input("Enter subject name : ")
# marks = int(input("Enter " + subject + " marks : "))
# dict.update({subject : marks})

# print(dict)






# # Store 9 and 9.0 as seperate values in set
# # s = {9,9.0}
# # print(s) Gives only one value

# # Solution 1 
# s = {"9","9.0"}
# print(s)

# # Solution 2
# s = {("int",9),("float",9.0)}
# print(s)







