'''
Given alist of tuples with info(name,subject):
* list all unique courses
*list student enrolled in english
*create dictionary(student,set of courses)
'''
# info={
#     ("Alice","Math"),
#     ("Bob","Science"),
#      ("Alice","Science"),
#      ("Charlie","Math"),
#      ("Alice","English"),
# }

# unique_courses = set()

# for tup in info:
#     unique_courses.add(tup[1])   

# print(unique_courses)   
# dict={} 
# for name,courses in info:
#     # if courses== "English":
#     #     print(name)
#     if dict.get(name)==None:
#         dict.update({name:set()})
#         dict[name].add(courses)
#     else:
#         dict[name].add(courses)

# print(dict)        

# Q1 Palindrome sequence
# String=input("Enter the string")
# if String==String[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not palindrome")    

# Q2
# list={1,4,5,6,6,8,20}
# total=0
# for a in list:
#     total+=a
# average=total/len(list)
# print("The average is",average)
#  Q3
# List1=[1,2,18,45,5]
# List2=[6,456,8,9]
# List3=List1+List2
# List3.sort()
# print("Your sorted list is here = ",List3)

#Q4
# integers=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# even_tuple=tuple(x for x in integers if x % 2==0)
# print(even_tuple)
# odd_tuple=tuple(x for x in integers if x %2 !=0)
# print(odd_tuple)

# Q5
# students={}
# while True:
#     print("\nMenu")
#     print("A. Add a student")
#     print("B. Update marks")
#     print("C. Search for a student")
#     print("D. Display all students and marks")
#     print("E. Exit")

#     choice = input("Enter the choice (A/B/C/D/E): ")

#     if choice == "A":
#         name = input("Enter the student name: ")
#         marks = int(input("Enter the marks: "))
#         students[name] = marks
#         print(f"Student {name} added successfully")

#     elif choice == "B":
#         name = input("Enter the student name to update marks: ")
#         if name in students:
#             marks = int(input("Enter the new marks: "))
#             students[name] = marks
#             print(f"Marks are updated for {name}")
#         else:
#             print("Student not found")

#     elif choice == "C":
#         name = input("Enter the student name you want to search: ")
#         if name in students:
#             print(f"{name} has {students[name]} marks")
#         else:
#             print("Student not found")

#     elif choice == "D":
#         if students:
#             print("Student records:")
#             for name, marks in students.items():
#                 print(f"{name}: {marks}")
#         else:
#             print("No student records available")

#     elif choice == "E":
#         print("Exiting the program... Bye!")
#         break

#     else:
#         print("Invalid choice")

        
#Q6
# words =["apple","banana","kiwi","cherry","mango"]
# word_length={}
# for word in words:
#     word_length[word]=len(word)
# print(word_length)
# Q7
# string=input("Enter the string")
# count_spaces=0
# for ch in string:
#     if ch==" ":
#         count_spaces+=1

# print(count_spaces)        
# Q8
# list1 =[1,2,3] 
# list2 =[3,4]
# set1=set(list1)
# # print(set1)
# set2=set(list2)
# # print(set2)
# if set1 & set2:
#     print("Common element exist",set1 & set2)
# else:
#     print("No common element found")    
# Q9
# list=[1,22,3,4,33,22,44,33]
# seen=set()
# duplicates=set()
# for item in list:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)
# print("The duplicates are",duplicates)    
#Q10
string=input("Enter the string") 
unique_chr=set(string)
print(unique_chr)
print(len(unique_chr))

                



     


    