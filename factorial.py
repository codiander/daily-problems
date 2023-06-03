#calculate factorial of a given number
def factorial(n):
    factorial=1
    if n==0 or n==1:
        return 1
    else:
         while n>1:
            factorial=factorial*n
            n=n-1
         return factorial

def trailing_zero(f):
    count = 0
    i = 5
    while (f//i != 0):
        count += int(f/i)
        i=i*5
    print("factorial of",f,"has",count,"trailing zeroes.")

print(factorial(9))
trailing_zero(10)

