import random
otp=random.randrange(10000,100000)
print(otp)
user=int(input('Enter the otp'))
if user==otp:
    print('Acces granted!!')
else:
    print('Acces denaid!!')