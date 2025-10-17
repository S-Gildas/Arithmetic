def list_abqr(a,b):
    
    """ This function gives a list of tuple , each tuple containing the value
           of a,b,q,r (q is the quotient, and r the remainder) ,
           from the last division to the first one. """
    
    r, q = a%b ,a//b # the remainder and the quotient of the division of a by b
    
    abrq_list=[] # abr_list will be the liste of tuple (a,b,q,r) for each divison

    while True :
        r, q = a%b ,a//b # and q, r
        abrq_list.append((a,b,q,r)) #add at the end of the list the triplet (a,b,r)
        a, b = b, r      # new values of a, b
        if r == 0:
            break
    abrq_list.reverse()
    
    return abrq_list

def get_bezout_coefficient_k(a,b,nth):

    """In the division of a by b ,this function gives the nth
        Bezout's coefficients x_n, y_n , at each step, from the
        last division to the first one such that we have : 
        x_n*a_n+y_n*b_n=r_n (r_n is the nth remainder) """

    q_values = tuple(zip(*list_abqr(a,b)))[2] # quotients values 
    n_steps=len(list_abqr(a,b))-1  # n_steps= total number of divisions made
                                   # The last division, with zero remainder
                                   # isn't counted
    if nth>=1 and nth <=n_steps:
        if nth == 1 : # Base case
            return 1, -q_values[nth] # x_1=1 and y_1=-q_1
        else:         # recursion case
            return get_bezout_coefficient_k(a,b,nth-1)[1], get_bezout_coefficient_k(a,b,nth-1)[0]-get_bezout_coefficient_k(a,b,nth-1)[1] * q_values[nth] # x_n=y_n_1 and y_n= x_n_1 - q_n * y_n_1
        
    

#def str_bezout(a,b,option,nth):
   # """Function which aims to facilitate the explanation of Bezout's relation """
    #x_n,y_n = get_bezout_coefficient_k(a,b,nth)
    #a_values, b_values, q_values, r_values = zip(*list_abqr(a,b)) # all values of
      # a,b,q and r
   # a_n, b_n, q_n, r_n =a_values[nth], b_values[nth], q_values[nth], r_values[nth]
   # if option == 1:
        #return f"{x_n}x{a_n} + {y_n}x{b_n}"
    #elif option == 2:
        #return  f"({a_n}-{q_n}x({str_bezout(a,b,2,nth+1)})  <=== :[since {r_n}={a_n}-{b_n}x{q_n}]."
  
    

def process_bezout_algorithm(a,b):

    """ This function gives the process of research of Bezout's relation :
        ax+by=d=gcd(a,b) """
    
    a_values,b_values ,q_values ,r_values = zip(*list_abqr(a,b)) # all values of a and r
    
    gcd=r_values[1] # the gcd of a and b is the last non-zero remainder
    
    print("\nThe great common divisor is the last non-zero remainder")
    print(f"gcd({a}, {b}) = {gcd}")
    print(f"\n=== Etapes successifs pour trouver une relation de Bezout entre {a} et {b} ===\n")

    n_steps=len(list_abqr(a,b))-1 # n_steps= total number of divisions made
                                   # The last division, with zero remainder
                                   # isn't counted
                                   
    k=1 # for the first print 
    x_k,y_k = get_bezout_coefficient_k(a,b,k)
    a_k, b_k = a_values[k], b_values[k]
    print(f"{gcd} = {x_k}x{a_k} + {y_k}x{b_k}\n")
    space=len(f"{gcd} ")*" "
    a_next, b_next, q_next = a_values[k+1], b_values[k+1], q_values[k+1]
    b_k_str=f"({a_next} - {q_next} x {b_next})"  # b_k 's expression
    print(f"{space}= {x_k}x{a_k} + {y_k} x {b_k_str}")
    print(f"{6*space} After the factorization of {a_k} we have :")
    
    for k in range(2,n_steps+1): # for other prints
        x_k,y_k = get_bezout_coefficient_k(a,b,k)
        a_k, b_k = a_values[k], b_values[k]
        
        print(f"{space}= {x_k}x{a_k} + {y_k}x{b_k}")
        if k<=n_steps-1:
            a_next, b_next, q_next = a_values[k+1], b_values[k+1], q_values[k+1]
            b_k_str=f"({a_next} - {q_next} x {b_next})"  # b_k 's expression
            print(f"{space}= {x_k}x{a_k} + {y_k} x {b_k_str}")
            print(f"{6*space} After the factorization of {a_k} we have :")

def print_divisions_made(a,b):
    """ This Functions prints all divisions made in the Euclide algorithm """
    
    a_values,b_values ,q_values ,r_values = zip(*list_abqr(a,b)) # all values of a and r
    
    #gcd=r_values[1] # the gcd of a and b is the last non-zero remainder

    #print(f"gcd({a}, {b}) = {gcd}")
    print(f"\n=== Divisions made in the Euclidian algorithm with {a} and {b} ===\n")

    n_steps=len(list_abqr(a,b))-1 # n_steps= total number of divisions made
                                   # The last division, with zero remainder
                                   # isn't counted
    
    for k in range(n_steps,0,-1):
        a_k, b_k, q_k, r_k = a_values[k], b_values[k], q_values[k], r_values[k]
        print(f"{a_k} = {b_k} x {q_k} + {r_k}")
    print()

if __name__=="__main__":
    a=1769 # a, b are non-zero  integers
    b=2379 # and a is not a muultiple of b and b is not a multiple of a
    print("_____________Chapter 1, Exercise 4_____________\n")
    print(f"1.What is the gcd of  {a} and {b} ? 2.Express it as a linear combination of these two numbers.\n\n")
    print_divisions_made(a,b)
    process_bezout_algorithm(a,b)
    
    
        
        
                                

     

     
     
            
    

    
    
    
    
    
         
    
