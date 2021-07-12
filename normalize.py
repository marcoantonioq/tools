#!/usr/bin/env python3
#coding: utf-8
# import subprocess
# subprocess.call(['pip3', 'install', 'subprocess'])

import re
import sys
from unicodedata import normalize


######
#  Removendo caractéres espéciais
def unicodeASCII(string):
    string = string.upper()
    string = normalize('NFKD', string).encode(
        "ASCII", "ignore").decode("ASCII")
    # Remover
    string = re.sub(u"[\.()%!\?\^\\\/#$]", '', string)
    # Remover espaços duplos
    string = re.sub(u" {2,}", ' ', string)
    # Remover espaços no inicio e no final
    string = string.strip()
    # Substituir por _
    string = re.sub(u"[ -]", '_', string)
    print(string)
    return string

if len(sys.argv) > 1:
    string = unicodeASCII(sys.argv[1])
    print(string)
    exit(0)
