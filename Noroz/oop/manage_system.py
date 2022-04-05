
from base64 import encode
import re
import hashlib
from collections import defaultdict

class Account():
    alluser=defaultdict(list)
    def __init__(self,user_name,password,phone_number,email):
        user_name=re.match('^[a-zA-Z]+\_[a-zA-Z]+$',user_name)
        password=re.match('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}',password)
        phone_number=re.match('^((989)|09)[0-9]{9}$',phone_number)
        email=re.match('^(\w|[._-])+@(\w|[._-])+\.([a-zA-Z]{2,5})$',email)
        if user_name:
            self.user_name=user_name.group()
            Account.alluser[self.user_name].append(self.user_name)
        else:
            raise Exception('invalid username')
        if password:
            password=hashlib.sha256(password.group().encode('utf-8')).hexdigest()
            self.password=password
            Account.alluser[self.user_name].append(self.password)
        else:
            raise Exception('invalid password')
        if phone_number:
            self.phone_number=phone_number.group()
            Account.alluser[self.user_name].append(self.phone_number)
        else:
            raise Exception('invalid phon number')
        if email:
            self.email=email.group()
            Account.alluser[self.user_name].append(self.email)
        else:
            raise Exception('invalid Email')
class Site():   
    def __init__(self,url,register_users,active_users):
        self.url=url
        self.register_users=register_users
        self.active_users=active_users
    def register(self,username):
        if username.user_name not in self.register_users:
            self.register_users.append(username.user_name)
            return 'register successful'
        else:
            raise Exception('user already registered')
    def login(self,password,email='',username=''):
        password=hashlib.sha256(password.encode('utf-8')).hexdigest()
        for val in Account.alluser.values():
            if val in self.active_users:
                return 'user already logged in'
            else:
                if username in self.register_users and password==val[1] and email==val[3]: 
                    self.active_users.append(val)
                    return 'login successful'
                elif username in self.register_users and password==val[1] and email=='': 
                    self.active_users.append(val)
                    return 'login successful'
                elif username==''  and password==val[1] and email==val[3] and val[0] in self.register_users: 
                    self.active_users.append(val)
                    return 'login successful'
                else:
                    return 'invalid login'
    def logout(self,object):
        for user in self.active_users:
            if object.user_name in user:
                self.active_users.remove(user)
                return 'logout successful'
            else:
                return 'user in not logout in'
    
user1=Account('mohamm_k','1245moHafff','09353992983','mo@ali.codd')
user2=Account('mohamm_l','041mohammaJ','09102425410','moh@amm.codd')
user3=Account('mohamm_j','041mohammaJ','09102425410','moh@amm.codd')
site=Site('www.',[],[])
print(site.register(user1))
print(site.register(user2))
print(site.register(user3))
print(site.login('1245moHafff',email='mo@ali.codd'))
print(site.login('1245moHafff',email='mo@ali.codd'))
print(site.logout(user1))



# site.login('1245moHafff')


