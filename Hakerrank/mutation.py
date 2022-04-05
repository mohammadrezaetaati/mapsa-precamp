
str=input()
nam,position=input().split()
print(position)
print(str[:int(nam)]+position+str[int(nam):])
