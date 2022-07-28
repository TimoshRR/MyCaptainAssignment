terms = int(input ("Enter the number of terms: "))  
n1 = 0  
n2 = 1  
count = 0  
if terms <= 0:  
    print ("The entered number is not valid, Please enter a positive number.")  
elif terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", terms, ": ")  
    print(n1)  
 
else:  
    print ("The fibonacci sequence of the numbers is: ")  
    while count < terms:  
        print(n1)  
        nth = n1 + n2  
        n1 = n2  
        n2 = nth  
        count += 1 
