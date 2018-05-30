#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
#doc=open('/home/dexter/text.txt')
for line in sys.stdin:
    ligne = line.strip()
    ligne=ligne.split(' ')
    print(ligne[0]+' '+ligne[1]+' '+str(ligne[2]))
