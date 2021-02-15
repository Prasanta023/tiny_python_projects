#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='This program Says Hello to the input name')
parser.add_argument('name',help='Name to greet ')
parser.add_argument('From',help='name of the place')
args = parser.parse_args()
print('Hello ' + args.name + ' from '+ args.From + '!')