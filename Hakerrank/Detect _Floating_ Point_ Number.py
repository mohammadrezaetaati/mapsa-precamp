from curses.ascii import isalpha, islower
a='4+6'
print(a.isalpha())
result=[]
number=int(input())
for _ in range(number):
    a=input()
    if a.startswith('-+') or a.endswith('.'):
        result.append('false')
        continue
    try:
        if isinstance(eval(a),float):
            result.append('True')
        else:
            result.append('False')
    except:
        result.append('False')
for ele in result:
    print(ele)
