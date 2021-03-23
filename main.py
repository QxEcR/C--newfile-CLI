import  os

os.system("touch main.cpp")
with open('main.cpp',"w+") as f:
    f.write("#include <iostream>\n")
    f.write("#include <string>\n")
    f.write("int main()\n{\n")
    f.write("   /* write your code here */\n")
    f.write("return 0;\n")
    f.write("}")