import mini2 
# import Library 
from UserDB import UserDB 


class Main:


    def login(self,name,password):
        for i,j in UserDB.user_object.items():
            if name==i and password==j.password:
                return j.role
        print("your name or password is wrong")

    def show_student_menu(self):
            self.current_user = mini2.Student(self.name,self.password)
    def show_admin_menu(self):
        self.current_user = mini2.Admin(self.name,self.password)
    

    def __init__(self):
        self.library_flag = True
        self.userDB_flag = True
        self.userDB = UserDB()
        # self.library = Library()

        
        self.current_user = None
        
        name =input("name?")
        password = input("password")

        role = self.login(name, password)
        if role == "admin":
            self.current_user = mini2.Admin(name,password)
            # show_admin_menu(self,name,password) 
        elif role == "student":
            self.current_user = mini2.Student(name,password)
            # show_student_menu()

        # self.show_admin_menu()

        while True:
            x = input("cıkmak için 'e'")
            if x == 'e':
                break 

    


main = Main()