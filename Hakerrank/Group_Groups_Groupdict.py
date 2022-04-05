import re
regex=re.search('([0-9a-zA-Z])\1+','mmcommit__')
a=regex.group()
print(a)