import re
def fun(s):
    regex=re.match('[\w -]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    if regex:
        return True
    else:
        return False