#!/usr/bin/env python3
#coding: utf-8

import sys
import os
import re
import pyperclip

import ssa

def clear(): return os.system('clear')

# from normalize import unicodeASCII
# unicodeASCII("Marco é Bonitão!")

def readFile(file):
    with open(file, 'r') as reader:
        return reader.read()

def writeFile(file, text):
    with open(file, 'w') as writer:
        return writer.write(text)
    
if len(sys.argv) > 1:
    file = sys.argv[1]
    result = readFile(file)


    for termo, string in ssa.termos.items():

        replaces = {
            f'^ +{termo},': f'  {termo} AS "{string}",',
            f' AS {termo},': f' AS "{string}",',
        }

        for regex, replace in replaces.items():
            # Formatar
            regex = re.compile(rf'{regex}', re.MULTILINE | re.DOTALL)
            result = re.sub(regex, f"{replace}", result) # re.IGNORECASE
        
        # pyperclip.copy(result)
    
    # clear()
    print(result)

    # writeFile(file, result)
    exit(0)
else:
    print("replacessa.py <file>")
    
