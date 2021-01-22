class MenuItem:
    def __init__(self,text,number):
        self.text=text
        self.number=number
    
    def display(self):
        return self.number,self.text



class Menu:
    def __init__(self,header):
        self.header=header
        self.menuItems=[]
    
    def display(self,display_header):
        if display_header:
            print(self.header)
        print(self.menuItems)  #?   
        
        
    def add_menu_item(self,text,number):
        obj=MenuItem(text,number)
        self.menuItems.append(obj)

#___________________________#



class User:
    menu = Menu("")
    menu_items=[]
    def __init__(self,name,password):
        self.name=name 
        self.password=password

    def display(self):
        return self.name, self.password     

    def menu_builder(self):
        # self.menu.menuItems = self.menu_items
        User.menu.menuItems = User.menu_items #!
        User.menu.display(True)
    

class Admin(User):
    menu="Welcome to admin menu"
    menu_items= ["List books", "Create a book", "Delete a book","Search for a book","Change number of a copies of a book", "Show students borrowed a book by ""ID","List Users", "Create User","Delete User", "Exit"]
    # super().menu.header ="absds"  # bu yanlışş
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role = "admin"
        User.menu.header = Admin.menu  # ... = self.menu de yazılabilir
        User.menu_items = self.menu_items
        super().menu_builder()  # class level olmadığı için super() ile erişim sağlandı

# obj = Admin("deneme",123)   # deneme amaçlı

class Student(User):
    menu_flag=False
    menu = "Welcome to student menu"
    menu_items = ["Search for a book", "Add a book to my book list", "delete a bookfrom my book list","show my borrowed books", "Exit"]
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role = "student"
        if Student.menu_flag == False:
            User.menu.header = Student.menu
            User.menu_items = Student.menu_items
            super().menu_builder()  # class level olmadığı için super() ile erişim sağlandı
            Student.menu_flag = True # ? olmalı mı
        else:
            User.menu.display(True) # menu oluşturulmuşsa menuyü göstersin


# print("s1 oluşturuldu")
# s1 = Student("s1",123)
# print("s2 oluşturuldu")
# s2 = Student("s2",123) 



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

# """ deneme amaçlı işin bitince kapat :P """
# db = UserDB()
# db.list_users()
# """   """


class Book:
    def __init__(self,bid,name,no_of_copies,list_of_authors):
        self.bid=bid
        self.name=name
        self.no_of_copies=no_of_copies
        self.list_of_authors=list_of_authors
    def display(self):
        return self.bid,self.name,self.no_of_copies,self.list_of_authors


class Library(Book):

    example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3,["Alice"]]}

    author_to_book={}
    book_object={}
    example_books_flag=True
    
    
    
    def add_book(self,bid,name,copies,authors):
        obj=Book(bid,name,copies,authors)
        Library.book_object[bid]=[name,copies,authors]
        for i,j in self.book_object.items():
            s=""
            for a in j[2]:
                s+=a
            if i not in self.author_to_book:
                Library.author_to_book[s]=obj
                # print(i,j)
            else:
                Library.author_to_book[s]=obj
                # print(i,j)
    
    def create_example_book(self):
            for i,j in self.example_books.items():
                # print(i,j)
                self.add_book(i,j[0],j[1],j[2])

    def __init__(self):
        if Library.example_books_flag:
            self.create_example_book()
            Library.example_books_flag=False

    def remove_book(self,bid):
        for i,j in self.book_object.items():
            if i==bid:
                del i
                self.author_to_book.pop(j[2])
    def list_book(self):
        a=[]
        for i,j in self.book_object.items():
            a.append(j[0])
        return a
    def search_book(self,name = "",author=""):
        for i,j in Library.book_object.items():
            if j[0]==name or j[2] == author:
                return i

    def update_book_copies(self,copy,name="",author=""):
        Library.book_object[self.search_book(name = name,author=author)][1] =copy


# l= Library()
# # l.list_book()
# # print(l.author_to_book)
# # print(l.book_object)

# print(l.search_book("Biology"))

# l.update_book_copies(9,"Biology")
# print(l.book_object)





