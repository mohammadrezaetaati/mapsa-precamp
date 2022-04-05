import re
user_input=input()
regex=re.split(r'[.,]',user_input)
print('\n'.join(regex))