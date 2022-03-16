import random

print('Welcome to your Password Generator')

chars = 'abcdelfghijklmnipqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?1234567890'

number = input('Amount of passwords to generate: ')
number = int(number)

lenght = input('Input your password lenght: ')
lenght =  int(lenght)

print('\npassword generated:')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
