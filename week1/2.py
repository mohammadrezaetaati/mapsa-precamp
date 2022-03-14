def even_odd(number):
    try:
        if (int(number)%2==0):
           return 'even'
        else:
           return 'odd'
    except ValueError:
        return "Please Enter a Number!!"
print(even_odd(input('Enter a Number: ')))