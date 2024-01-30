def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count


n1 = int(input("Enter first range: "))
n2 = int(input("Enter last range: "))
    
for i in range(n1, n2 + 1):
        count = is_prime(i)
        if count == 2:
            print(i, end='\t')

    