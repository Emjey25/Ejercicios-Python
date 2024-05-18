
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
password = ''

lengthPW = int(input('que longitud quieres para tu pw: '))

for _ in range(lengthPW):
    password += random.choice(chars)
print(password) 