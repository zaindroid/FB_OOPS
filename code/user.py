

class User():
    def __init__(self, first_name,last_name,user_name,password,age,interest):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.interest=interest
        self.friends=[]
        self.groups=[]
        self.user_name=user_name
        self.password=password

    def register(self):
        

        # this function needs to appnd new user to MAINFRAME users attribute
        pass
         
        
    def login(self, user_name,password):

        if user_name!=self.user_name:
            msg="username not correct"
            login_status=False
        elif password!=self.password:
            msg="Password not correct"
            login_status=False
        else: 
            msg=" Login in successfull "
            login_status=True
        
        return msg,login_status





        user_name=input("Please enter your user name")
        password=input("Please enter your password")



        
    
    
    def set_username(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def set_friends(self,friend):
        self.friends=self.friends.append(friend)

    def get_friends(self):
        return [x for x in self.friends]

    
    def set_group(self,group):
        self.groups=self.groups.append(group)

    def get_groups(self):
        return [x for x in self.groups]

            

        
