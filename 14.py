try:
    a = int(input('enter first number'))
    b = int(input('enter second number'))
    print(a / b)
    r = open('filenotexsist.txt')
except ZeroDivisionError:
    print('could not divide by zero')
except FileNotFoundError:
    print('file not found')

print('end of program 102/65')
