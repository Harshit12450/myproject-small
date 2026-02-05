# with open("sample.txt","r") as f:
#     data =f.read()
#     print(data)
# import os
# os.remove("sample.txt")

# Problem
# data=True
# word="python"
# line=1
# with open("sample2.txt","r") as f:
#     while data:
#         data=f.readline()

#         if word in data:
             
#             print(f"{word} is on line no {line}")
#             break
#         line+=1

# Exception handling
# try:
#     x=int(input("Enter the value of x: "))
#     div=10/x

# except ZeroDivisionError:
#     print(f"Divide by zero is not allowed")
# except ValueError:
#     print("Invalid input")

# else:
#     print(f"The answer is {div}")           
# finally:
#     print("End of the program")

# List Comprehension
# sq=[i*i for i in range(1,7) if i%2 !=0]
# print(sq)
# num=[1,-4,-5,8,9,-13]
# num=[0 if val <0 else val for val in num]
# print(num)
# words=["Python","Hello","English"]
# words=[val.upper() for val in words]
# print(words)

# JSON MODULE
# import json
# # py_obj={"name":"Shraddha","isteacher":"True"}
# # # json_str='{"name":"Shraddha","isteacher":true}'
# # # py_obj=json.loads(json_str)
# # json_str=json.dumps(py_obj)
# # print(type(json_str))
# # with open("data.json","r") as f:
# #     py_obj=json.load(f)
# #     print(py_obj)
# d={"name":"Harshit","age":28,"isteacher":"True"}
# with open("data.json","w") as f:
#     json.dump(d,f,indent=4)

# Assignment Question
# Q1
# with open("sample2.txt","w+") as f:
#     f.writelines(["Harshit Yadav\n","Himanshu Singh\n","Gaurav\n","Prashant\n","Nandan\n"])
    
# with open("sample2.txt","r") as a:
#     data=a.read()
#     print(data)

# Q2
# with open("log.txt","a") as f:
#     data=f.write("program run successfully")
# with open("log.txt","r") as a:
#     data=a.read()
#     print("Log file",data)  

# Q3
# numbers=[5,10,15,20,25]
# num=[n for n in numbers if n>15]
# print(num)

# Q4


# import json
# cities={
#     "Delhi":10000,
#     "Haryana":86495,
#     "Uttar Pradesh":54546,
# }
# with open("cities.json","w") as f:
#     json.dump(cities,f)

# with open("cities.json","r") as f:
#     data=json.load(f)
# print("Current cities and populations")
# for city,population in data.items():
#     print(f"{city} and {population}")

# new_city=input("Enter a new city")
# population=input("enter the population of the city you entered")
# data.update({new_city:population})  
# with open("cities.json","w") as f:
#     json.dump(data,f)

# print("Updated solution and population:")
# for city,population in data.items():
#     print(f"{city}:{population}")

# Q5
try:
    with open("data.txt","r") as f:
        data=f.read()
        print("data")
except FileNotFoundError:
    print("Oops Your File not exist")  
finally:
    print("Come agin good luck")          







    

    



 
