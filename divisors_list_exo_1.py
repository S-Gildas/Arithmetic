def divisors_list(given_number):
    """ Chapter 1, Exercise 1
        This function takes an integer n and returns
        a list of its positives divisors. """
    
    divisors=[] # initialization of the divisors's list
    
    for number in range(1,given_number+1): # n's divisors are between 1 and n
        if given_number % number == 0: # if number | n, we will add it to the list
            divisors.append(number)
    return divisors

if __name__ == "__main__":
    
    # liste des diviseurs de 36, 59 et 30

    print("_____________Chapter 1, Exercise 1_____________\n")
    print("Write the complete list of divisors in N of 36, 59 and 30.\n")
    print(f"List of 36's divisors : {divisors_list(36)}")
    print(f"List of 59's divisors : {divisors_list(59)}")
    print(f"List of 30's divisors : {divisors_list(30)}")
            
