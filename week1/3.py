def max_min(number1,number2,number3)->int:
    try:
        numbers=[int(number1),int(number2),int(number3)]
        return f'max is: {max(numbers)} \nmin is: {min(numbers)}'
    except ValueError:
        return "Please Enter a Number!!"

print(max_min(input('Enter the first number: '),input('Enter the second number: '),input('Enter the third number: ')))



