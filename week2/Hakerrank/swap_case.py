input_str=input('Enter String :')
for chr in input_str:
    if chr.islower():
        print(chr.upper(),end='')
    elif chr.isupper():
        print(chr.lower(),end='')
    else:
        print(chr,end='')