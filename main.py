import  os

os.system("touch main.cpp")
with open('main.cpp',"w+") as f:
    f.write("""
            #include <iostream>\n
            #include <string>\n\n
            using namespace std;\n\n
            int main()\n{\n
               /* write your code here */\n
               return 0;\n
            }
    """)