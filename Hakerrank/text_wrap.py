import textwrap
# def wrap(string,max_width):
#     count=-1
#     for chr in string:
#         count+=1
#         if count==max_width:
#             print()
#             count=0
#         print(chr,end='')
# wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)
a=textwrap.TextWrapper(width=4)
b=a.wrap(text='ABCDEFGHIJKLIMNOQRSTUVWXYZ')
for i in b:
    print(i)
