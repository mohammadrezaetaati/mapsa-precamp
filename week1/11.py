from random import randint
rand=randint(1,20)
try:
    for count in range(1,6):
        user_input=int(input(f'Enter your guesse({count}):'))
        if(user_input==rand):
            print('You win')
            break
    else:
        print(f'Game Over \nCorrect Answer:{rand}')
except ValueError:
    print('Please Enter a Number!!')