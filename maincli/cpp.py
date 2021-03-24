import os

def is_file_exist(filename):
    files = os.listdir('.')
    for file in files:
        if file == filename:
            return True
    return False

def create_file(filename):
    open(filename, 'a').close()

def is_type_valid(methodtype):
    list = ["char","string","bool","int","void"]
    if methodtype in list:
        return True
    return False

def write_header(filename):
    with open(filename,"a+") as f:
        f.write("#include <iostream>\n")
        f.write("#include <string>\n\n")
        f.write("using namespace std;\n\n")
        
def write_method(filename,methodname,methodtype):
    with open(filename,"a+") as f:
        f.write(f"{methodtype} {methodname}()")
        f.write("\n{\n   /* write your code here */\n")
        f.write("   return;\n")
        f.write("}\n\n")

def write_main(filename):
    with open(filename,"a+") as f:
        f.write("int main()\n{\n")
        f.write("   /* write your code here */\n")
        f.write("   return 0;\n")
        f.write("}")
        

def create_cpp(argv):
    if len(argv) == 1:
        os.system("echo give a name for the file")
        exit()
    
    """
        get the file name and check if exist
    """
    filename = argv[1]
    filename += ".cpp"
    if is_file_exist(filename):
        os.system("echo file already exist!")
        exit()
    
    """
        create the file
    """
    create_file(filename)
    """
       write the headers 
    """
    write_header(filename)
    """
        get the methods names and types and check if type is valid
    """
    args = argv[2:]
    for arg in args:
        methodname = arg.split(":")[0]
        methodtype = arg.split(":")[1]
        if not is_type_valid(methodtype):
            os.system(f"echo type {methodtype} is invalid")
            exit()
        write_method(filename,methodname,methodtype)
    
    """
        write main method
    """
    write_main(filename)