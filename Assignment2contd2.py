#Write a Python program to print all positive numbers in a range.
num = int(input("Enter the number of values you want to enter into the list: "))
lst = []
positive_lst = []

for i in range(num):
    value = int(input("Enter: "))
    lst.append(value)
print("The original list: ",lst)

for val in lst:
    if val>=0:
        positive_lst.append(val)
print("The positive list: ",positive_lst)
    
