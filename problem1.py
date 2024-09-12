# 1. Exploring Python's OS Module

#Task 1: Directory Inspector
import os

def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Directory not found")
    except PermissionError:
        print("Insufficient permissions to access directory or file")
    except Exception as e:
        print("An error occurred: ", e)
    #end try
#end function
        
path = input("Enter a directory: ")
list_directory_contents(path)