def is_perfect_integer(n):
    somme=0
    for diviseur in range(1,n):
        if n%diviseur==0:
            somme=somme+diviseur
    return (somme==n)

if __name__=="__main__" :
    from divisors_list_exo_1 import divisors_list
    print("_____________Chapter 1, Exercise 11_____________\n")
    print("Verify that 6, 28, 496, 8128 are perfects numbers.")
    perfects=[6,28,496,8128]
    for k in perfects:
        print(f"{k}'s divisors are : ", divisors_list(k))
        print(f"is_perfect_integer({k})={is_perfect_integer(k)}")
    print()
    print("Perfects numbers between 1 and 10.000 are :")
    print()
    for k in range(1,10001):
        if is_perfect_integer(k):
            print(k,end="__")
    print("only")
