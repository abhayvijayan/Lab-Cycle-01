# IF ELIF ELSE
is_active = True
if is_active:
    print('Hello i am Active!')

number = 10
if number >= 5:
    print('number greater than 5!')

# IF ELSE
if number > 5:
    print('hi')
else:
    print('Hello')

# NESTED IF
if number > 2:
    if number >= 5:
        print('hello world!')

# IF ELIF LADDER
if number > 10:
    print('10')
elif number > 5:
    print('5')
else:
    print('blahhh')


# FOR LOOP
for i in range(1, 11):
    print(i)

# LOOPING IN LIST
fruits = ['apple', 'orange', 'cherry', 'banana', 'plum']
for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if fruit == 'banana':
        print('Found it!')
        break
    else:
        print('checking..',fruit)


# WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1


available = True
while available:
    print('hi i am available!')
    available = False


# BREAK AND CONTINUE
num = 10
for i in range(num + 1):
    if i == 2:
        print('Skipping...')
        continue
    if i == 5:
        print('Reached 5... Exiting')
        break

    print(i)