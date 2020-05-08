class Frame():
    '''This is the main parent class that holds all the runtime data of the users groups and there activities '''
    def __init__(self):
        
        self.users=[] # must contain user objects as list enteries, a user object will have all the info with it

    def add_user(self,new_user):
        self.users.append(new_user)

    def delete_user(self,user_name):

        '''search for specific user based on user name and if exits then delete it from records'''
        flag=0
        for i in self.users:
            flag+=1
            if i.user_name==username:
                 del_user=self.users.pop(i)
                 return print("user {} has been removed",format(del_user.first_name))
            elif flag==len(self.users):
                return print("No user found with this user name")               
            else:
                continue

    def search_user(self,username):
        '''search for specific user based on user name'''
        flag=0
        index=0
        user_obj=None
        for user in self.users:
            flag+=1
            
            if user.user_name==username:
                msg="User found"
                user_obj=user
                return msg,user_obj  ##returns the user object from list of the registered users 
            elif flag==len(self.users):
                msg="No user found with this user name"
                user_obj=None
                return msg,user_obj   
            else:
                index+=1
                continue



    def show_wall(self):
        '''Displays general posts from all the users '''
        flag=0
        for i in self.users:
             flag+=1
             if self.users[i]!=None:
                 print ("{} says: {}".format(self.users.first_name,self.users.status))
                 print("===================")
            
class User(Frame):
    def __init__(self, first_name,last_name,user_name,password,age,interest):
        super().__init__()
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
            msg=" Login successfull "
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

            

        
