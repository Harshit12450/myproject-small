# class Laptop:
#     storage_type="SSB"

#     def __init__(self,RAM,storage):
#         self.RAM=RAM
#         self.storage=storage

#     def get_info(self):
#         print(f"Your laptops has {self.RAM} RAM {self.storage} storage {self.storage_type}")    

# L1=Laptop("16GB","512GB")   
# L2=Laptop("8gb","256gb")
# L1.get_info()     

# PRODUCT STORE
# class Products:
#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         Products.count+=1

#     def get_info(self):
#         print(f"Your product name is {self.name} and price is {self.price} ")

#     @classmethod   
#     def get_count(cls):
#         print(f"Your count is {cls.count}")

#     @staticmethod
#     def calc_discount(price,discount):
#         final_price=price-(discount*price/100)
#         print(f"Your discounted price is {final_price}")




# P1=Products("Laptop",100000)
# P2=Products("Phone",20000)
# P1.get_info()
# P1.calc_discount(P1.price,10)

# Encapsulation
# class Bankaccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance #Private 

#     def get_balance(self):#Get function used to get private value
#         return self.__balance
#     def set_balance(self,new_balance):#Set used to set new value
#         self.__balance=new_balance
        

# Acc1=Bankaccount("Harshit",20000)
# Acc1.set_balance(20000000)
# print(Acc1.name,Acc1.get_balance())

# Multiple Inheritance
# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary

# class student:
#     def __init__(self,cgpa):
#         self.cgpa=cgpa

# class TA(Teacher,student):
#     def __init__(self,name, salary,cgpa,):
#         super().__init__(salary)
#         student.__init__(self,cgpa)
#         self.name=name

# Ta1=TA("Harshit",15000,9.2)
# print(Ta1.name,Ta1.salary,Ta1.cgpa)

# Abstraction
# from abc import ABC, abstractmethod
# class Animal:
#     def make_sound(self):
#         pass

# class Lion:
#     def make_sound(self):
#         print("Roar")

# class Cow:
#     def make_sound(self):
#         print("MOO")

# L1=Lion()
# C1=Cow()
# L1.make_sound() 
# C1.make_sound()                   

# class Bankaccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.balance=balance
        
#     def deposit(self):
#         enter=int(input("How much you want to enter ?"))
#         self.balance+=enter
#         print(f"Your deposit money is {enter} and current balance is {self.balance}")

#     def withdraw(self):
#         enter1=int(input("How much money you want to withdraw ?"))
#         if enter1>self.balance:
#             print("Insuffiecent balance")
#         else: 
#             self.balance-=enter1
#         print(f"Your withdrawn amount is{enter1} and current balance  is {self.balance}")     

        

#     def check_balance(self):
#         print(f"Your account has balance of  ${self.balance} ")      

    



# acc1=Bankaccount(112233,"Harshit",20000)  
# acc1.deposit()
# acc1.withdraw()
# acc1.check_balance()   

# Q2
# class Book:
    
#     review_count=0
   
#     def __init__(self,title,author,list_of_review):
#         self.title=title
#         self.author=author
#         self.list_of_review=list_of_review if list_of_review else []
       

#     def add_review(self):
#         review=input("Tell us about your review")
#         self.list_of_review.append(review)
#         Book.review_count+=1
#         print(f"Your review is added in {self.list_of_review}")

#     @classmethod 
#     def get_count_review(cls):  
#         print(f"Your reveiw count is {cls.review_count}")  

#     def display(self):
#         print(f"ALL the reviews are:{self.list_of_review}")    


# b1=Book("Jumanji","JK","")
# b1.add_review()       
# b1.add_review()
# b1.get_count_review()
# b1.display()        
        
# Q3
# class student:
#     def __init__(self,name,roll_no,marks):
#         if not name.strip():
#             raise  ValueError("Name value can't be empty")
#         self.__name=name

#         if (1<=roll_no<=100):
#             raise ValueError("Roll no is invalid")
#         self.__roll_no=roll_no

#         if marks<0:
#             raise ValueError("INVALID")
#         self.__marks=marks

#     def get_name(self):
#         return self.__name  
#     def get_roll_no(self):
#         return self.__roll_no
#     def get_marks(self):
#         return self.__marks
    

# s1=student("Harshit",112233,90)
# print(s1.get_name(),s1.get_roll_no(),s1.get_marks())     
        
#Q4
# import math
# class shape:
#     def area(self):
#         raise NotImplementedError("SUBCLASSES")

# class circle(shape): 

#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return 3.14*self.radius*self.radius

# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length*self.breadth   

# class triangle(shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height

#     def area(self):
#         return 1/2*self.base*self.height


# r1=rectangle(3,4)
# c1=circle(5)
# print(c1.area())

# print(r1.area())
# Q5
# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# class car(vehicle):
#     def __init__(self, brand, model,seat_in_car):
#         super().__init__(brand, model)
#         self.seat_in_car=seat_in_car

# class bike(vehicle):
#     def __init__(self, brand, model,engine_cc):
#         super().__init__(brand, model)   
#         self.engine_cc=engine_cc

# b1=bike("Royal enfield",2025,350)
# print(f"Your bike brand is {b1.brand} and model is {b1.model} and engine is {b1.engine_cc} cc")

# Q6
# from abc import ABC,abstractmethod
# class employee:
#     def calculate_salary(self):
#         pass

# class intern(employee):
#     def calculate_salary(self):
#         print("As an intern you will get 10000 pr month")

# class fulltimeemployee(employee):
#     def calculate_salary(self):
#         print("AS an full time employee you will get 100000 per month") 

# class contract_employee(employee):
#     def calculate_salary(self):
#         print("He will be paid on the basis of contract listed")

# i1=intern()
# i1.calculate_salary()
# Q7
# class person:
#     def __init__(self,name,age=None,address=None):
#         self.name=name
#         self.age=age
#         self.address=address

#     def show_details(self):
#         if self.age is None and self.address is None:
#             print(f"Name:{self.name}")

#         elif self.address is None:
#             print(f"Name:{self.name} and age: {self.age}") 
#         else:
#             print(f"Name:{self.name} age: {self.age} address:{self.address}")

# p1=person("Harshit")
# p2=person("Arun",21)
# p3=person("hero",21,"Beta1 greater noida")
# p1.show_details()
# p2.show_details()
# p3.show_details()
        
#Q8 
# class player:
#     player_count=0
#     def __init__(self,name,level):
        
#         self.name=name
#         self.level=level
#         player.player_count+=1

#     @classmethod
#     def get_count(cls):
#         print(f"Your player count is {cls.player_count}")    

# p1=player("Sachin","INTERNATIONAL LEVEL")     
# P2=player("Virat","International level")
# print(p1.name,p1.level)
# player.get_count()

# Q9
# class hervivore:
#     def eat(self):
#         print("The animal which eat grass")

# class carnivore:
#     def eat(self):
#         print("The animal which hunt their prey and then eat")

# class omnivore:
#     def eat(self):
#         print("Animal which depend on both hervivore and carnivore")

# class bear(hervivore,carnivore,omnivore):
#     def eat(Self):
#          hervivore.eat(Self)
#          carnivore.eat(Self)
#          omnivore.eat(Self)
#          print("Bear can eat both plants and animals")
# b1=bear()
# b1.eat()
# print(bear.__mro__) # mro = means method resolution order it call all the parent methods
   
# Q10 OOP chat system
class User:
    def __init__(self, username, gmail):
        self.username = username
        self.gmail = gmail

    def __str__(self):
        return f"Username is: {self.username} and mail id is {self.gmail}"


class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender.username}: {self.content}"


class Chatroom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join_room(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.username} joined room {self.room_name}")

    def leave_room(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left {self.room_name}")

    def send_message(self, user, content):
        if user in self.users:
            msg = Message(user, content)
            self.messages.append(msg)
            print(f"{user.username} sent a message: {content}")
        else:
            print(f"{user.username} is not in the chatroom. Cannot send message.")

    def view_history(self):
        print(f"\nChat history of {self.room_name}:")
        for msg in self.messages:
            print(msg)


# Example usage
u1 = User("Harshit", "hy90388@gmail.com")
u2 = User("Prashant", "subhashkumar1234@gmail.com")
u3 = User("Neha", "neha@example.com")

room = Chatroom("Python Batch")
room.join_room(u1)
room.join_room(u2)
room.send_message(u1, "Hello Everyone!")
room.send_message(u2, "Hi Harshit, how are you?")
room.send_message(u3, "Can I join?")
room.join_room(u3)
room.send_message(u3, "Now I can chat!")
room.view_history()
room.leave_room(u2)
            


        

        

    
    
  
   




        


        

        

            
        

       


    


        
     



    
        