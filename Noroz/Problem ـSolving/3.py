from operator import index


def well_defined(str):
    for chr in range(len(str)):
        if str[chr]=='?' and chr!=0:
            if str[chr-1]=='0':
                str=str.replace('?','1',1)
            else:
                str=str.replace('?','0',1)
        elif str[chr]=='?' and chr==0:
            if str[chr+1]=='0':
                str=str.replace('?','1',1)
            else:
                str=str.replace('?','0',1)
    for i in range(len(str)-1):
        if str[i]==str[i+1]:
            return 'khosh Tarif nist'
            break
    else:
        return 'khosh Tarif hast'

print(well_defined('0??10'))

