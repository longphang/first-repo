import os
import sys


def read_file(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def main():
    print('Hello World - this is on branch test1')


if __name__ == '__main__':
    main()
