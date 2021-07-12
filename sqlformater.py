#!/usr/bin/env python3
#coding: utf-8

# Doc
# https://buildmedia.readthedocs.org/media/pdf/sqlparse/latest/sqlparse.pdf

import sqlparse
import re

# import subprocess
# subprocess.call(['pip3', 'install', "sqlparse"])


def readFile(file):
    with open(file, 'r') as reader:
        return reader.read()
    
sql = readFile("teste.txt")

# Separar mais de uma consulta em segmentos
statements = sqlparse.split(sql)

print(statements[0])
# print(statements[1])
# print(re.findall(r'FROM.*(WHERE|)', statements[0]))


# parsed = sqlparse.parse(sql)
# print(sqlparse.format(statements[0], reindent=True, keyword_case='upper'))