from parser import *
import os
import sys


def main():
    s = b"hi\n"
    sys.stdout.buffer.write(s)


if __name__ == '__main__':
    main()
