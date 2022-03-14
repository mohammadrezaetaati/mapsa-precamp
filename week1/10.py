message='Babak Khorramdin'
print(message[0])
print('----------------------------')
print(message[6])
print('----------------------------')
for chr in message.split():
    print(chr)
print('----------------------------')
for word in range(2,12,2):
    print(message[word])
print('----------------------------')
for word in message:
    if(word=='m'):
        print('True')
        break

