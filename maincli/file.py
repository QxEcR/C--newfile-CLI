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