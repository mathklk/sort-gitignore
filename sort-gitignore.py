#!/usr/bin/python3
import os

file = os.getcwd() + '/.gitignore'

if not os.path.exists(file):
    print('No .gitignore file found in the current directory ' + os.getcwd())
    exit()

with open(file, 'r') as f:
    lines = f.readlines()

sorted_lines = sorted([x.strip() for x in lines])

with open(file, 'w') as f:
    f.write('\n'.join(sorted_lines))