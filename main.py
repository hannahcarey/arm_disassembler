from parser_utils import *
import os
import sys


def parser():
    s = b"hi\n"
    sys.stdout.buffer.write(s)


if __name__ == '__main__':
    parser()
