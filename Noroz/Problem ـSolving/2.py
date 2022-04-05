def shortening(number):
    shortening_list=[]
    for n in range(len(number)-1):
        shortening_list.append(int(number.replace(number[n:n+2],str(int(number[n])+int(number[n+1])))))
    print(shortening_list)
    print(max(shortening_list))
        

shortening('10038')


