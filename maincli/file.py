import os


# os.system("touch main.cpp")
# with open('main.cpp',"w+") as f:
#     f.write("#include <iostream>\n")
#     f.write("#include <string>\n\n")
#     f.write("using namespace std;\n\n")
#     f.write("int main()\n{\n")
#     f.write("   /* write your code here */\n")
#     f.write("   return 0;\n")
#     f.write("}")


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
