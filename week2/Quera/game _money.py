


class Account:
    def __init__(self,usernam,password,user_id,phone,email):
        self.usernam=usernam
        self.password=password
        self.user_id=user_id
        self.phone=phone
        self.email=email
    def show_welcome(self):
        usernam=self.usernam.replace('_',' ') 
        usernam=usernam.title()
        if(len(usernam)>15):
                return f'welcome to our site {usernam[:15]}...'
        return f'welcome to our site {usernam}'
    def hash_password(self,hash='hash'):
        password=''
        for char in self.password:
            if(hash=='hash'):
                ord_chr=ord(char)+10
            elif(hash=='unhash'):
                ord_chr=ord(char)-10
            password=password+chr(ord_chr)
        self.password=password
        return self.password

    def verify_change_password(self,oldpassword,newpasword):
        if(oldpassword==self.hash_password('unhash')):
            self.password=newpasword
            return self.password
        else:
            return 'old password is wrong'

        
        
mohammad=Account('kianoush_nasr','12',12,56899,454)
print(mohammad.show_welcome())
print(mohammad.hash_password())
print(mohammad.hash_password('unhash'))


print(mohammad.verify_change_password('12',1400))
