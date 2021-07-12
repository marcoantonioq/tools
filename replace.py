#!/usr/bin/env python3
#coding: utf-8

import sys
import os
import re
import pyperclip

def clear(): return os.system('clear')

# from normalize import unicodeASCII
# unicodeASCII("Marco é Bonitão!")

def readFile(file):
    with open(file, 'r') as reader:
        return reader.read()

if len(sys.argv) > 3:
    file = sys.argv[1]
    regex = sys.argv[2]
    string = sys.argv[3]

    # Formatar
    regex = re.compile(rf'{regex}', re.MULTILINE | re.DOTALL)

    result = re.sub(regex, string, readFile(file)) # re.IGNORECASE
    
    pyperclip.copy(result)
   
    clear()
    print(result)

    exit(0)
else:
    print("replace.py <file> <regex> <str>")
    
