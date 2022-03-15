def merge_the_tools(string, k):
    n=len(string)//k
    distinct_str=[]
    for chr in range(0,len(string),n):
        
        for i in range(chr,chr+n):
            if string[i] not in distinct_str:
                distinct_str.append(string[i])
                print(string[i],end='')
        distinct_str.append('')
        print()




merge_the_tools('AAABCADDE',3)
