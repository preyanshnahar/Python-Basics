# File Input/Output
# Types of Files
# Text File     : .txt , .docx , .log
# Binary Files  : .mp4 , .moc , .png , .jpeg






# # File Open
# # Syntax 
# Default mode is Read
# f = open("file_name","mode")
# data = f.read()
# f.close()
# If file is in same folder then directly name.txt else full path







# f = open("temp.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()







# Character | Meaning
# 'r'       | open for reading (default)
# 'w'       | open for writing, truncating the file first
# 'x'       | create a new file and open it for writing
# 'a'       | open for writing, appending to the end of the file if it exists
# 'b'       | binary mode
# 't'       | text mode (default)
# '+'       | open a disk file for updating (reading and writing)







# f.read()      -> Reads entire file
# f.read(n)     -> Reads first n characters
# f.readline()  -> Reads one line at a time






# f = open("temp.txt","w")
# f.write("This is new code")
# f.close()

# f = open("temp.txt","r")
# data = f.read()
# print(data)







# f = open("temp.txt","a")
# f.write("\nThis is new line")
# f.close()

# f = open("temp.txt","r")
# print(f.read())








# # With Syntax
# with open("filename.txt","a") as f :
#     data = f.read()







# with open("temp.txt","r") as f :
#     data = f.read() 
#     print(data)
#     f.close() # Not Required since with automatically closes the file








# # Deleting a File -> Using Module
# import os
# os.remove("temp.txt")








# # Create a new file and add data
# f = open("temp.txt","a+")
# f.write("Preyansh\nNahar\n21")
# f.close()






# # Replace all occurrences of Java with Python
# f = open("temp.txt","r")
# data = f.read()
# f.close()
# data = data.replace("Java","Python")
# f = open("temp.txt","w")
# f.write(data)
# f.close()








# # Search if the word x exists in file
# f = open("temp.txt","r")
# data = f.read()
# if(data.find("Preyansh") != -1) : print("Found")
# else : print("Not Found")








# Find the line in which x occur first, if not print -1
# f = open("temp.txt","r")
# fl = False
# i = 1
# while(True) :
#     data = f.readline()
#     if(data == "") : break
#     if(data.find("Preyansh") != -1) : 
#         print("Found at : ",i)
#         fl = True
#         break
#     i += 1
# f.close
# if(not fl) : print(-1)












# Count even numbers in a file containing comma seperated numbers
f = open("temp.txt","r")
data = f.read()
nums = data.split(",")
count = 0 
for i in nums :
    if(int(i) % 2 == 0) : count += 1
print(nums)
print(count)
f.close()
