from curses.ascii import isalnum, isalpha, isdigit, islower, isupper
from collections import defaultdict




string='a2222'
validtors=(isalnum,isalpha,isdigit,islower,isupper)
print(any(chr.isalnum() for chr in string))
print(any(chr.isalpha() for chr in string))
print(any(chr.isdigit() for chr in string))
print(any(chr.islower() for chr in string))
print(any(chr.isupper() for chr in string))


