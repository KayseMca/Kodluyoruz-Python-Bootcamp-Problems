from mini2 import Admin
from mini2 import Student



class UserDB:
    example_users = {'Ahmet': ['1234', 'student'], 'Ayse': ['4321', 'student'], "admin":["0000", 'admin']}
    user_object ={} # key:kullanıcı adı value:User objesi olmalı !!!
    example_users_flag = True

    def add_user(self,name, password, role):
        obj = 0
        if role=="admin":
            obj = Admin(name, password)
        elif role == "student":
            obj = Student(name, password)
        else:
            raise("role parametresi admin veya student olmalı")
        UserDB.user_object[name]=obj

    def create_example_users(self):
        for i,j in UserDB.example_users.items():
            self.add_user(i,j[0],j[1])
            print("\n------\n",j[1],"\n------\n") # deneme amaçlı
    
    def __init__(self):
        
        if UserDB.example_users_flag == True:
            self.create_example_users()
            UserDB.example_users_flag = False

    def remove_user(self): # hangi user silinecek ? 
        pass

    def list_users(self):
        for i,j in UserDB.user_object.items():
            print(i,j.role)
            print(i, j.name,j.password,j.role)

if __name__ == "__main__":
    db = UserDB()
    print(db)