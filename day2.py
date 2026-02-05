# Q1 
# Salary=int(input("State your salary :"))
# if Salary>30000:
#     print("Your tax will be 5%")
# elif Salary<70000:
#     print("Your tax will be 15%")
# elif Salary<70000:
#     print("Your tax will be 25%")
# else:
#     print("You are not elligible") 

#Q2 
# def integer(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
# a=int(input("Enter the no:"))
# b=int(input("Enter the no:"))           
# print(integer(a,b))

# Q3
# n=312
# for i in str(n):
#     print(i)

#  method 2
# n=312
# while n>0:
#     digit=n%10
#     print(digit)
#     n=n//10

# Q4
# def TOTAL_DIGIT(N):
#     N=abs(N)
#     LENGTH=len(str(N))
#     print(LENGTH)

# TOTAL_DIGIT(8427)

# Q5
# for i in range(1,101):
#     if i%3 ==0 and i%5==0:
#         print(i)

# Q6
# n=int(input("Enter your number: "))
# if n>0:
#     print("The number is positive")
# elif n<0:
#     print("The number is negative")
# else:
#     print("You typed the wrong input")    
# Q7
# def calculator(a,b,operation):
#     if operation=="+":
#         return a+b
#     elif operation=="-":
#         return a-b
#     elif operation=="*":
#         return a*b
#     elif operation=="%":
#         if a>b:
#             return a%b
#         else:
#             print("This is not possible")

#     else:
#         print("There is no other operation specified")

# print(calculator(5,6,"+"))   

# Q8
# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=int(input("Enter your number :"))
# print(is_prime(n))
# Q9
# n=5
# i=1
# while i<=10:
#     mul=n*i
#     print(n,"*",i,"=",mul)
#     i+=1


# while True:
#     user_says=input("What you want to say number or quit")
#     if user_says.lower() == "quit":
#         print("project terminated")
#         break
#     try:

#         n=int(user_says)

#     except ValueError:
#         print("Pls enter a valid number")
#         continue
    
#     if n > 0:
#         print("Positive")
#     elif n<0:
#         print("Negative")
#     else:
#         print("Are you mad what are you entering")        
        
# def isprime(n):
#     if n<=1 :
#         return False
#     elif n==2:
#         return True
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# print(isprime(7))    
# secret_word="Honest"
# guess_word=input("Guess your word: ").lower()
# min_length=min(len(secret_word),len(guess_word))
# match_count=0
# for i in range(min_length):
#     if secret_word[i]==guess_word[i]:
#         match_count+=1

# accuracy=(match_count/len(secret_word))*100
# print(f"accuracy:{accuracy:.2f}%")

# if guess_word==secret_word:
#     print("It's a perfect a match")
# else:
#     print("Better luck next time")            

# numbers=[1,2,3,4,5,6,7,8,9,17,17,19]
# sum=0
# for num in numbers:
#     sum+=num
# print(sum)


d = { "name": "Shradha",
      "subjects":["math", "science", "physics"],
      "cgpa": 9.5 }
for key, value in d.items(): 
    print(key, value)






        


        
    
    




    

  
    


           
