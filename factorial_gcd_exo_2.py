""" Code for Chapter 1, exercice 2. """

def gcd(number_1, number_2):

    """ This function return the great common divisor
        of two integers number_1 and number_2 by using Euclide's
        algorithm.  """

    #        Euclide's Algorithm
    
    remainder= number_1 % number_2
    
    while remainder !=0:
        number_1, number_2 = number_2, remainder
        remainder= number_1 % number_2

    return number_2 # The last non-zero remainder is the gcd

def factorial(number):

    """ This function return the factorial of an integer 'number' using recursion """
    
    if number == 0 : # base case
        return 1
    else :           # recurrence case
        return number * factorial(number-1)
        

if __name__=="__main__":

    print("_____________Chapter 1, Exercise 2_____________\n")
    print("""We can prove that n!+1 and (n+1)!+1 are coprime for all positive integer n.
             We will verify that for  n from 1 to 30 \n\n""")
    for k in range(1,31):
        print(f"gcd({k}!+1, {k+1}!+1) = gcd({factorial(k)+1},{factorial(k+1)+1}) = {gcd(factorial(k)+1,factorial(k+1)+1)}")             
    
    
        
    

    
         
