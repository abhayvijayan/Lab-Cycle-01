choice = 0
balance = 0

while True:
    print('#########################')
    print(' 1 ----- WITHDRAW        ')
    print(' 2 ----- DEPOSIT         ')
    print(' 3 ----- CHECK BALANCE   ')
    print(' 4 ----- EXIT            ')
    print('#########################')
    choice = int(input('Enter your choice : '))

    if choice == 1:
        if balance <= 0:
            print('Oops!..You dont have enough balance!... press enter to continue..')
            input() # FOR WAITING BEFORE CONTINUE
            continue
        else:
            amount = int(input('Enter amount : '))
            if amount <= 0:
                print('Oops!.. Expecting a number greater than 0!... press enter to continue..')
                input() # FOR WAITING BEFORE CONTINUE
                continue
            else :
                balance -= amount
                print(f'Successfully Withdrawed Rs.{amount}... press enter to continue..')
                input() # FOR WAITING BEFORE CONTINUE
                continue
    elif choice == 2:
        amount = int(input('Enter amount : '))
        if amount <= 0:
            print('Oops!...Expecting a number greater than 0!... press enter to continue..')
            input() # FOR WAITING BEFORE CONTINUE
            continue
        else:
            balance += amount
            print(f'Credited Rs.{amount} to your account!... press enter to continue..')
            input() # FOR WAITING BEFORE CONTINUE
            continue
    elif choice == 3:
        print(f'Your balance is Rs.{balance}... press enter to continue..')
        input() # FOR WAITING BEFORE CONTINUE
        continue
    elif choice == 4:
        print('Exiting....')
        break
    else:
        print('Oops!...Not a valid choice! press enter to continue..')
        input() # FOR WAITING BEFORE CONTINUE
        continue

        