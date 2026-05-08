# # String Concatenation
# a = "Preyansh"
# b = "Nahar"
# print(a+" "+b)




# Length of a string
# a = "Preyansh Nahar"
# print(len(a))
# b = 20
# print(len(b)) #int type does not have len






# Escape sequence characters
#  \n -> Next Line
#  \t -> Tab Space
#  \t -> Tab Space






# Indexing
# a = "Preyansh"
# # print(a[10]) # Invalid
# print(a[0]) # Valid
# a[0] = "r" # Invalid
# print(a)
# print(a[0])






# # Slicing
# temp = "Preyansh"
# #  P   r   e   y   a   n   s   h
# #  0   1   2   3   4   5   6   7
# # -8  -7  -6  -5  -4  -3  -2  -1

# print(temp[0:5])     # Start from index 0 to 4
# print(temp[:5])      # Default start index is 0
# print(temp[5:])      # Prints from index 5 till end
# print(temp[:])       # Prints complete string

# print(temp[-1])      # Last character
# print(temp[-3:])     # Last 3 characters
# print(temp[:-3])     # Excludes last 3 characters
# print(temp[-5:-1])   # From index -5 to -2

# print(temp[::2])     # Prints every 2nd character
# print(temp[1::2])    # Prints odd indexed characters
# print(temp[::3])     # Prints every 3rd character

# print(temp[::-1])    # Reverses the string
# print(temp[::-2])    # Reverse with step 2
# print(temp[7:2:-1])  # Reverse from index 7 to 3
# print(temp[3:1:-1])  # Reverse from index 3 to 2

# print(temp[3:1])     # Empty output because step is +1
# print(temp[-1:-5])   # Empty output because step is +1

# print(temp[:100])    # No error even if end exceeds length
# print(temp[100:])    # Empty output because start exceeds length










# String Functions
# str = "preyansh nahar"
# print(str.endswith("sh")) # returns true if found
# print(str.capitalize()) # Capitalized first character of each word, Does not change the original value, only prints the string with changes
# print(str.replace("r","e")) # replace all occurances
# print(str.find("er")) # Gives the index of first occurence
# print(str.count("a")) # gives count of all occurences










# # Write a program to take name input and print its length
# name = input("Enter your name : ")
# print(len(name))






# # Write a program to find the occurence of '$' in String
# name = input("Enter your name : ")
# print(name.find('$')) 
# print(name.count('$')) 






# Conditional Statements 
# age = int(input("Enter your age : "))
# if(age >= 18) :
#     print("you can drive")
# elif(age >= 16) :
#     print("learners license")
# else : print("Cannot Drive")







# # Write a prgram to check even/odd number
# num = int(input("Enter your number : "))
# f = (num%2 == 0)
# if(f) :
#     print("Even")
# else :
#     print("Odd")







# # Write a program to find greatest of three numbers
# num1 = int(input("Enter num 1 : "))
# num2 = int(input("Enter num 2 : "))
# num3 = int(input("Enter num 3 : "))

# if(num1 >= num2) :
#     if(num1 >= num3) :
#         print("Greatest : ",num1)
#     else :
#         print("Greatest : ",num3)
# else :
#     if(num2 >= num3) :
#         print("Greatest : ",num2)
#     else :
#         print("Greatest : ",num3)










# Write a program to check if a number is multiple of 7
# num = int(input("Enter your number : "))
# print(num % 7 == 0 and num > 0) 










