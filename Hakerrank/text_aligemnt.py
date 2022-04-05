

print('H'.center(10,'-'))
print('HHH'.rjust(6,' '))
print('HHHHH'.rjust(7,'-'))
print('HHHHHhh'.rjust(8,' '))
print('HHHHHhhhh'.rjust(9,' '))


a=5
input_user=int(input('Enter thickness :'))
space=input_user
for i in range(input_user):
    if i==0:
        print(' '*input_user+'H')
    else:
        space=space-1
        print(' '*space+'H'*(i+1))