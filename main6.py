# Functions in python
# def sum(a,b) :
#     return a + b

# a = 10 
# b = 2
# print(sum(a,b))





# A function can have no return statement
# A function can have no parameters as input
# # Syntax
# def func_name(param1 , param2) :
#     return param1 * param2

# print(func_name(arg1,arg2))







# Types of functions 
# Built In Functions -> print() , len() , type() ,range()
# User Defined Functions -> Defined by user







# # Default Parameter -> Used when no arguments are passed
# First Non default arguments are passed then default arguments
# def mul(a=1,b=1) :
#     return a*b
# print(mul(10))
# print(mul(10,20))
# print(mul())








# # Write a function to print len of list
# def list_len(a) :
#     i = 0
#     for el in a :
#         i += 1
#     return i

# a = [1,2,343,12,1,2,3,1,2]
# print(list_len(a))







# # Write a function to print the elements of a list in a single line
# def list_print(a) :
#     for el in a :
#         print(el,end=" ")
# a = [1,2,343,12,1,2,3,1,2]
# list_print(a)






# # Write a function to find factorial of a number
# n = int(input("Enter your number : "))
# def fact(n = 1) :
#     fact = 1
#     for i in range(1,n+1) : fact *= i
#     return fact
# print(fact(n))







# # Convert USD to INR
# n = int(input("Enter value in USD : "))
# def usd_to_inr(n = 0) :
#     print(n * 100)
# usd_to_inr(n)







# # Write a function to print even or odd
# n = int(input("Enter your number : ")) 
# def eo(n) :
#     if(n%2 == 0) : print("EVEN")
#     else : print("ODD")

# eo(n)







# # Recursion
# # Function calls itself
# n = int(input("Enter your number : "))
# def rec(n) :
#     if(n == 0) : return # Base Case
#     print(n) 
#     rec(n-1)
# rec(n)






# # Factorial
# n = int(input("Enter your number : "))
# def fact(n) :
#     if(n <= 1) : return 1 
#     return n * fact(n-1)
# print(fact(n))









# # Write a program to calculate the sum of first n natural numbers
# n = int(input("Enter your number : "))
# def sum(n) :
#     if(n <= 0) : return 0 
#     return n + sum(n-1)
# print(sum(n))






# # Using recursion print all elements in a list
# ls = [1,2,3,4,12,123,1123123]
# def p(ls,i) :
#     if(i == len(ls)) : return 
#     print(ls[i])
#     p(ls,i+1)
# p(ls,0)