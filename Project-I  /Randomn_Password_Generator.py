import random
			
print('Password Generator')
			
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(?+'
number=input('Enter number of passwords')
number=int(number)
length=input('Enter the length of the password')
length=int(length)
for pwd in range(number):
    pas=''
    for c in range(length):
        pas=pas+random.choice(chars)
    print(pas)
