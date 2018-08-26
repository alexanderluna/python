for i in range(2, 1000):
    j = 2
    prime = True
    while j < i:
        if i % j == 0:
            prime = False
        j = j + 1
    if prime:
        print(str(i) + " is a prime number")
