def f(n):
    "give the nth term of Fibonacci's sequence"
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+f(n-2)



if __name__=="__main__":
    from factorial_gcd_exo_2 import gcd

    print("_____________Chapter 1, Exercise 3____________\n")
    print("f(n) is the nth term of Fibonacci sequence \n")
    print("""\n 1. We can prove that gcd(f(n),f(n+1))=1 for all integer n>=0\n
          We'll verify that for n from 1 to 10\n""")
    for n in range(11):
        print(f"gcd(f({n}),f({n+1}))=gcd({f(n)},{f(n+1)})={gcd(f(n),f(n+1))}")
    print("""\n 2. But it'is false to say that every f(n) and f(m) are coprime (m!=n).\n""")
    print(f"f(2)={f(2)} and f(5)={f(5)} are not coprime for example.")
    
