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
    list = ["char","String","boolean","int","void"]
    if methodtype in list:
        return True
    return False

def write_header(filename):
    with open(filename,"a+") as f:
        f.write(f"class {filename[:len(filename) - 5]}")
        f.write("{\n")
        f.write("    public static void main(String []args){\n")
        f.write("        /* write your code here */\n")
        f.write("    }\n")
        
def write_last_curly_bracket(filename):
    with open(filename,"a+") as f:
        f.write("}")
        
        
def write_method(filename,methodname,methodtype):
    with open(filename,"a+") as f:
        f.write(f"    public {methodtype} {methodname}()")
        f.write("{\n")
        f.write("        /* write your code here */\n")
        if methodtype == "String":
            f.write("        return \"\";\n")
        elif methodtype == "int":
            f.write("        return 0;\n")
        elif methodtype == "char":
            f.write("        return 'a';\n")
        elif methodtype == "boolean":
            f.write("        return true;\n")
        f.write("    }\n")

        

def create_java(argv):
    if len(argv) == 1:
        os.system("echo give a name for the file")
        exit()
    args = argv[2:]
    for arg in args:
        methodname = arg.split(":")[0]
        methodtype = arg.split(":")[1]
        if not is_type_valid(methodtype):
            os.system(f"echo type {methodtype} is invalid")
            exit()
    """
        get the file name and check if exist
    """
    filename = argv[1]
    filename += ".java"
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
    write_last_curly_bracket(filename)