# main memory
d = {}
j=4
# PC incrementing after each iteration
for i in range(j):
    print('memory: ',d)
    interrupt = input("Would you like to issue an interrupt? ")
#taking input
    if interrupt == 'yes':
        val = int(input('Enter a value:'))
        # updating main memory
        d[i]=val
    
