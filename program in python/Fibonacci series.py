ft = 0
st = 1
n = int(input("Enter No. of Terms: "))
    
print(f"Fibonacci Series = {ft}, {st}", end=", ")
    
for i in range(1, n-1):
    nt = ft + st
    print(f"{nt}", end=", ")
    ft, st = st, nt