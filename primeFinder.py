#get starting value
user_start = input("Enter a starting value ")
#get ending value
user_end = input("Enter an ending value ")
increment = user_start
count = 2
prime = 1
#find if each value in the range is prime or not
#increment is every number between the user_start and user_end
for increment in range(user_end):
    #count is every number between 1 and increment
    for count in range (increment):
        #if increment is evenly divided by count, then it cannot be prime
        #prime == 1 means the value is prime, prime == 0 means it is not prime
        if(increment % count == 0):
            prime = 0
    if(prime == 1):
        print(increment+" is prime")
    else:
        print(increment+" is not prime")