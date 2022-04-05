number_input=int(input())
save_error=[]
for n in range(number_input):
    try:
        a,b=map(int,input().split())
        save_error.append(a//b) 
    except ZeroDivisionError :
       save_error.append('integer division or modulo by zero')
    except ValueError as e:
       save_error.append(e)
for error in save_error:
    if isinstance(error,int):
        print(error)
    else:
        print('Error Code:',error)
      



