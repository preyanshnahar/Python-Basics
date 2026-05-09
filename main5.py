# Loops in python

# While Loop
# Syntax
# while(condition) :
#     statement

# num = 12 
# while(num > 0) :
#     num -= 1
#     print(num)

# num = 1 
# while(num > 0) :
#     print(num) # infinite loop








# # Print numbers from 1 to 5
# num = 1 
# while(num <= 5) :
#     print(num)
#     num += 1






# # Print numbers 1 to 100
# i = 1 
# while i <= 100 : 
#     print(i)
#     i += 1






# # Print numbers 100 to 1
# i = 100
# while i >= 1 : 
#     print(i)
#     i -= 1






# # Print multiplication table of a number n
# n = int(input("Enter your number : "))
# i = 1 
# while(i <= 10) : 
#     print(n, "*", i, "=", n*i)
#     i += 1








# # Print Elements of a list
# ls = [1,2,3,4,12,213,12]
# i = 0 
# n = len(ls)
# while(i < n) :
#     print(ls[i])
#     i += 1







# Search for a number x in a list
# ls = [1,2,3,4,12,213,12]
# f = False
# i = 0
# n = len(ls)
# ele = int(input("Enter the element to be found : "))

# while(i < n) :
#     if(ls[i] == ele) :
#         print("Found")
#         f = True
#         break
#     i += 1
# if(not f) : print("Not Found")







# Break -> Used to break the loop
# Continue -> Used to skip the current iteration






# # For Loop
# nums = [1,2,3,4,12,21,31]
# for num in nums :
#     print(num)





# # For Loop eith else -> After loop ends it prints the else part
# for num in nums : 
#     print(num)
# else : print("End")






# # Range is used to traverse from i = start till i < end 
# for i in range(1,10) :
#     print(i)








# # Write a program to find x in a list
# ls = [1,2,3,4,12,34]
# x = int(input("Enter your number : "))
# for i in ls :
#     if(i == x) : 
#         print("Found")
#         break 
# else : print("Not Found")






# Range -> sequence of numbers
# (start,end,step)
# Default start = 0 
# Default step = 1 





# # Pass -> It is a null statement
# for i in range(1,100) : 
#     pass









# # Find the sum of first n numbers
# n = int(input("Enter your number : "))
# sum = 0
# for i in range(n+1) :
#     sum += i
# print(sum)






# # Write a program to find factorial of first n number
# n = int(input("Enter your number : "))
# fact = 1 
# for i in range(1,n+1) :
#     fact *= i 
# print(fact)