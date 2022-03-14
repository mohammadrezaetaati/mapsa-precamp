try:
    width=int(input('Please Enter the width:'))
    length=int(input('Please Enter the length:'))
    for n in range(1,length):
        if (n==1):
            print(' '*(length-n)+'*'*width)
        else:
            print(' '*(length-n)+'*'+' '*(width-2)+'*')
    print('*'*width)
except ValueError:
    print('Please Enter a Number!!')


