#recursive factorial

def factorial(n):
    result=0
    if n<=1:
        result=1
    else:
        result=n*factorial(n-1)
    
    return result

print(factorial(5))