import sys

from .cpp import create_cpp
from .java import create_java

def cpp():
    create_cpp(sys.argv)
    
def java():
    create_java(sys.argv)