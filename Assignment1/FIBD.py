//code for the FIBD exercise, from the Rosalind website

NofMonths = 
lifelenght = 
Fib=[1]*100
for i in range(2,NofMonths):
    Fib[i]=Fib[i-1]+Fib[i-2]
    if i>=lifelenght:
        Fib[i]-=Fib[(i-lifelenght)-1]  
print(Fib[i])

