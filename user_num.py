#Detecting Even numbers from users

#Algorith
# 1. Ask the user about his number
# 2. Check if the input from the user is even
# 3. If so print a congratulations message to the user

while True:
    user_num = int(input('Enter your number: '))

    mode    =   user_num % 2

    if mode != 0:
        print('Sorry you entered an Odd number')
        print('')

    else:
        print('Congratulations your number is even') 