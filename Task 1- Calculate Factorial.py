
def factorial(result):
    if result<=1:
        return 1
    else:
        return result*factorial(result-1)


n=int(input("Enter a number: "))
print('Factorial of ',n,' is:',factorial(n));
