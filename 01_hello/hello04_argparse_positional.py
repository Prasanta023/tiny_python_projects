#!/usr/bin/env python3
# Purpose: Say hello

import sys
import argparse

# using argparse to read parameters
parser = argparse.ArgumentParser(description='This Program accepts a file name and the path')
parser.add_argument('name',help='FileName ',type=str)
parser.add_argument('Path',help='Directory path ',type=str)
# try:
args = parser.parse_args()
print('File Name: ',args.name)
print('File Path:',args.Path)

# using the sys argv to read the input parameter
print(len(sys.argv))
print(sys.argv[0],sys.argv[1],sys.argv[2])
