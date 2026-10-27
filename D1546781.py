k = 3
for i in range(k):
    for j in range(k - i):
        print('*', end='')
    print()
    
k = 3
for i in range(1, k + 2):
    for j in range(k - i + 1):
        print('*', end='')  
    print()
