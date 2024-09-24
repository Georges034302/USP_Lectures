#!/bin/env python3

import re 

s = 'UTS FEIT - USP Spring 2024 - python3'

print(re.search('p',s)) # finds first pattern occurrence
print(re.findall('p',s)) # finds all occurrences of the pattern
print(re.findall('p',s,flags=re.IGNORECASE)) # owrking like grep 

print(re.sub('\\d','-',s)) # working like sed
print(re.sub('[A-Z]','#',s))
