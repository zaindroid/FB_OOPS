from frame import Frame,User
#from user import User

'''This is the main script for the program that does all the user experience'''

fb=Frame()

def register_user():
    flag_attempt=0
    while flag_attempt<3:
        first_name=input("Please enter your first name: ")
        last_name=input("Please enter your last name: ")
        age=input("Please enter your age: ")
        interest=input("Please enter your interest: ")
        user_name=input("Please select your user name: ")
        password1=input("Please select your password: ")
        password2=input("Please confirm your password one more time: ")
        if password1!=password2:
            flag_attempt+=1
            print("password does not match..try again")
            continue
            if flag_attempt==3:
                print("You have exceeded maximum atempt limit")
                flag_attempt=0
                break
        else:
            
            new_user=User(first_name,last_name,user_name,password1,age,interest)
            print(''' 
            =====================================
                 New User added Successfully")
            =====================================
            ''')
            fb.add_user(new_user)
            break



def login_user():

    flag_attempt=0
    while flag_attempt<3:
        flag_attempt+=1

        user_name=input("Please enter your user name: ")
        password1=input("Please enter your password: ")

        msg,user_ins=fb.search_user(user_name)
        if user_ins!=None:
            msg,login_status= user_ins.login(user_ins.user_name,user_ins.password)

            if login_status:
                print(msg)

                ##go to dashboard
        else: 
             print('''
         ==================================
         No user found with this info
         ==================================
             
             ''')







opt_in=True
while opt_in:
   # print("Welcome to Zeebook")
    print("""
        Welcome to Zeebook

        1. Register as new user
        2. login into your accout
        3. exit     
          """)

    opt_in=input("Please chose an option in menu")

    if opt_in=="1":
        ##  user class
        print("Adding new user...")
        register_user()
    elif opt_in=="2": 
        ##  user class--login method
        print("You can login with your user password")

        login_user()
    elif opt_in=="3":
        exit()






    
