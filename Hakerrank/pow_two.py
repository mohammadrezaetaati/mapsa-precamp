
def number_pow_two(num:int):
    count_pow_two,pow=0,0
    while True:
        if 2**pow==num:
            count_pow_two=count_pow_two+1
            return f'The number of powers of this number is equal to:{count_pow_two}'
        elif num==1:
        	return f'The number of powers of this number is equal to:{count_pow_two}'
        elif 2**pow>num:
            pow-=1
            num=num-2**pow
            count_pow_two=count_pow_two+1
            pow=0
        pow+=1
        
    

        


print(number_pow_two(24))


