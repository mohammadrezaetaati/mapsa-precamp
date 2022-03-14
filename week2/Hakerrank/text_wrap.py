def wrap(string,max_width):
    count=-1
    for chr in string:
        count+=1
        if count==max_width:
            print()
            count=0
        print(chr,end='')
wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)
        