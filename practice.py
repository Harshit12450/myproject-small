# list=input[list]
# for i in list:
#     cal_avg=sum(list)/len(list)
# print(f"average of list is {cal_avg:.2f}")
# list1=[1,2,6,7]
# list2=[2,4,5]
# merge_list=list1+list2
#print(merge_list)
#print(sorted(merge_list))

# t=(1,2,3,4,5,6,7,8,9,10,11,12)
# evenlist=[]
# oddlist=[]
# for val in t:
#     if val%2==0:
#         evenlist.append(val)
#     else:
#         oddlist.append(val)
# EVENTUPLE=tuple(evenlist)
# ODDTUPLE=tuple(oddlist)
# print("Even tuple is =",EVENTUPLE)    
# print("Odd tuple is =",ODDTUPLE)     

# words =["apple","banana","kiwi","cherry","mango"]
# dict={}
# for val in words:
#     cal_len=len(val)
#     dict[val]=cal_len
# print(dict)
# l1=[1,2,3,4,5]
# l2=[6,7,8,9]
# S1=set(l1)
# S2=set(l2)
# if S1 & S2:
#     print("There is common elements")
# else:
#     print("Common element not present")    
# l1=[1,22,3,33,44,44,55,66,77,55,33]

# seen=set()
# duplicate=set()
# for val in l1:
#     if val in seen:
#         duplicate.add(val)
#     else:
#         seen.add(val) 

# print(duplicate)        

# string =input("Enter the string here")
# unique_chr=[]

# for ch in string:
#     if string.count(ch)==1:
#         unique_chr.append(ch)
    
# print(unique_chr)
# print(len(unique_chr))
 
# students={}

# while True:
#     print("\n Menu")
#     print("A. Add a Student")
#     print("B. Update Marks")
#     print("C.Search for a student")
#     print("D.Display all student and marks")
#     print("E. Program exited")

#     user_choice=input("Enter the choice ").lower()
    # if user_choice== "a":
    #     name=input("Enter the students name").lower()
    #     marks=int(input("Enter the marks"))
    #     students[name]=marks
    #     print("Student added successfully")

    
    # elif user_choice == "b":
    #     name = input("Enter student name to update: ").lower()
    #     if name in students:
    #         marks = int(input("Enter new marks: "))
    #         students[name] = marks
    #         print("Marks updated successfully.")
    #     else:
    #         print("Student not found.")

    # elif user_choice== "c":
    #     name=input("Enter the name of student you want to search").lower()
    #     if name in students:
    #         print(f"{name} scored {students[name]} marks")  
    #     else:
    #         print("Student not found")

    # elif user_choice=="d":
    #     if students:
    #        for name,marks in students.items():
    #            print(name,marks)     

    #     else:
    #         print("No student records found")  

    # elif user_choice=="e":
    #     print("program exited")
    #     break
    # else:
    #     print("invalid choice")                      
   

# finally it worked

class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
        Product.count+=1

    def get_info(self):
        print(f"Tour product name is {self.name} and its price is {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Your count will be {Product.count}")

    def discount_price(self,price,discount):
        print(f"Your discounted price will be {price - (price*discount/100)}")


p1=Product("Lapto",78000)
p2=Product("Pen",20)
p3=Product("Phone",20000)

p1.get_info()
p1.get_count()
p1.discount_price(20000,10)
        



  

        


