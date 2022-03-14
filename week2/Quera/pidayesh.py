def find(num1,num2,num3):
    user_input=[num1,num2,num3]
    for number in range(1,5):
        if(number not in user_input):
            return f'guess :{number}'
print(find(1,4,3))