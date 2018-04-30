import os
from subprocess import call

def main():
    print 'starting main'
    print call(["python", "-c", 'import test; print test.f("hi","there")'])


main()
