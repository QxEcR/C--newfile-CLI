# import  os

# os.system("touch main.cpp")
# with open('main.cpp',"w+") as f:
#     f.write("#include <iostream>\n")
#     f.write("#include <string>\n\n")
#     f.write("using namespace std;\n\n")
#     f.write("int main()\n{\n")
#     f.write("   /* write your code here */\n")
#     f.write("   return 0;\n")
#     f.write("}")

import sys

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

if __name__ == '__main__':
    main()