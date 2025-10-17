from math import sqrt

def liste_decomposition(n):
    """ Fonction qui retourne une liste contenant des couples (a,b) des 
    diverses décompositions possibles de l'entier n de la forme n=a*b"""

    m=int(sqrt(n))
    liste=[]

    for i in range(1,m+1):
        if n%i==0:
            liste.append((i,int(n/i)))
    return liste

def is_prime_number(n):
    m=int(sqrt(n))
    d=2
    while d<=m:
        if n%d==0:
            return False
        d+=1
    return True

def mersenne(p):
    return 2**p-1


if __name__=="__main__":
    print("Primalité des nombres de Mersenne Mp pour p allant de 2 à 40\n")
    for p in range(2,41):
        if is_prime_number(p):
            if is_prime_number(mersenne(p)) :
                print(f"M{p}={mersenne(p)} est un nombre premier\n")
            else:
                print(f"M{p}={mersenne(p)} n'est pas un nombre premier")
                print("Sa décomposition est :",liste_decomposition(mersenne(p)))
                print()
            
            
            
            
