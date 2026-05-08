# # Lists
# # Can be of any data type
# # Lists can slices similar to Strings
# temp = [1,2,2,3,4]
# print(temp)
# print(type(temp))
# print(temp[1])
# temp = [] # can be fully altered
# print(temp)
# temp = [1,2,3,4,5]
# print(temp)
# temp[0] = 100 # values can be changed 
# print(temp)
# temp = [1,"preyansh",2] # can have multiple data types
# print(temp)
# print(temp[0])
# print(type(temp[0]))
# print(temp[1])
# print(type(temp[1]))
# print(len(temp)) # can find length






# Strings -> Immutable
# List -> Mutable








# # List Methods
# l = [1,2,3,4,5]
# l.append(0) # Appends value at end
# l.sort() # Sorts list in ascending order
# l.sort(reverse=True) # Sorts in reverse
# l.reverse() # Reverses the list
# l.insert(2,3) # inserts like (index,value) 
# l.remove(1) # Removes first occurence of a element(value)
# l.pop(2) # Remove value at given index (ex: here index 2 is removed)








# # Tuples
# # Creates a immutable list
# tup = (1,2,3,4)
# print(tup)
# print(type(tup))
# # tup[0] = 2 # Invalid
# print(tup[0])
# print(len(tup))
# # We can initialize empty tuple
# tupp = ()
# print(tupp)
# # We can initialize empty index but only the last value and also only one empty
# t = (1,2,)
# print(len(t))
# print(t)










# a = (1) # Not a tuple
# print(type(a))

# b = (1,) # Tuple
# print(type(b))








# # Tuple Methods
# t = (12,23,13,24,23)
# print(t.index(23)) # Returns first index of the given value
# print(t.count(23)) # Returns count






# # Write a program to ask user to enter name of their 3 favorite movie and store them in list
# m1 = input("Enter movie 1 : ")
# m2 = input("Enter movie 2 : ")
# m3 = input("Enter movie 3 : ")
# l = [m1,m2,m3]
# print(l)






# Write a program to check if list contains a palindrome of elements
# t1 = [1,2,3,4]
# t2 = [1,2,2,1]

# # temp1 = t1.copy().reverse() # Invalid and returns None type
# temp1 = t1.copy()
# temp1.reverse()
# temp2 = t2.copy()
# temp2.reverse()

# print(t1 == temp1)
# print(t2 == temp2)








# # Write a program to count number of "A" grades in a tuple
# tup = ("A","B","C","A","A","D","C")
# print(tup.count("A"))





# # Store the above tuple in list and sort them from A to D
# l =  ["A","B","C","A","A","D","C"]
# print(l)
# l.sort() 
# print(l)