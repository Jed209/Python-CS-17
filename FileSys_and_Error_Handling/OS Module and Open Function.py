import os

#This asks for a file name, then creates the "file_name" variable
file_name = input("Choose a filename: ")
#This uses the OS module command to ping Google, then prints the ping results in the file name you created into a txt file.
os.system(r"ping 8.8.8.8 >> " + file_name + ".txt")

#This opens the file in read-only, and creates the "file" variable
with open(file_name + ".txt", "r") as file:
    #If ms string is located in the file, print statement
    if "ms" in file.read():
        print("You have an internet connection")
    #Otherwise, print this statement.    
    else:
        print("You do not have an internet connection")
    