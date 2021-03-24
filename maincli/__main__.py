import sys
import os
from sys import platform
from .file import create_file_win,create_file,is_file_exist,is_type_valid


def main():
    """
        get the file name and check if exist
    """
    filename = sys.argv[1]
    filename += ".cpp"
    if is_file_exist(filename):
        os.system("echo file already exist!")
        exit()
    
    """
        create the file
    """
    # create_file(filename)
    """
       write the headers 
    """
    
    """
        get the methods names and types and check if type is valid
    """
    args = sys.argv[2:]
    for arg in args:
        methodname = arg.split(":")[0]
        methodtype = arg.split(":")[1]
        if not is_type_valid(methodtype):
            os.system(f"echo type {methodtype} is invalid")
            exit()
    """
        write the methods
    """
    
    """
        write main method
    """
if __name__ == '__main__':
    main()
