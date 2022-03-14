def my_multiple(x,y):
    try:
        count=1
        sum=0
        while(count<=y):
            sum=sum+x 
            count+=1
        return sum
    except TypeError:
        return "Please Enter a Number!!"
print(my_multiple(2,3))
