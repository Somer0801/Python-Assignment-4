#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Task_1
#1. Make a calculator using Python with addition , subtraction ,multiplication ,division and power.
def add(a, b):
    return a + b

def subtract(a, b):
    return x - y

def multiply(a, b):
    return x * y

def divide(a, b):
    return a / b

def power(a,b):
    return a**b


print("Select operation.")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
print("Power")

while True:
    choice = input("What operator you want to use: ")

    if choice in ('+', '-', '*', '/' ,'^'):
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        elif choice =='^':
            print(num1, "^", num2, "=", power(num1,num2))
            next_calculation = input("Do you want to do more calculations? (yes/no): ")
            if next_calculation == "no":
                break
    
    else:
        print("Invalid Input")


# In[ ]:


#Task_2
# 2. Write a program to check if there is any numeric value in list using for loop.
Array = ["Mango","Omer",1,"Python",2,10] 
for i in list: 
    if type(i) == int: 
        print(f"{i} integer is present")


# In[ ]:


# Task_3
# Write a Python script to add a key to a dictionary.
Bio_data = {"Name":"Ammad", "Age": 20, "Roll_no":"19B_015_CS"}
Bio_data["Department"]="Computer Science"
Bio_data


# In[ ]:


#Task 4
# Write a Python program to sum all the numeric items in a dictionary.
data = {'English':89,'Maths':97,'Computer':92}
print(sum(data.values()))


# In[ ]:


# Task 5
# Write a program to identify duplicate values from list.
Fruits=["Mango","Apple","Kiwi","Mango","Banana","Kiwi"]
Fruits2=[]
for i in Fruits:
    if i not in Fruits2:
        Fruits2.append(i)
    else:
        print(i,end=' ')


# In[ ]:


#Task 6
#Write a Python script to check if a given key already exists in a dictionary
keys = {2:4 ,3:9 ,4:16 ,5:25 ,6:36}
def key_presence(x):
    if x in keys:
        print('your entered key is present in the dictionary')
    else:
        print('your entered key is not present in the dictionary')
key_presence(4)
key_presence(2)

