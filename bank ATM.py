balance = 50000

while True:
    print("\n ===WELCOME=== ")
    pin  = int(input("enter pin number: "))
    if pin == 1234:
        print("continue")

    else:
        print("invalid pin, Try again1")
        break
    print("1. check balance")
    print("2. amount withdraw")
    print("3. amount deposit")
    print("4. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        print("your balance is: ", balance)

    elif choice == "2":
        amount = int(input("enter your amount: "))

        if balance < amount:
            print(f"insufficient balance")

        elif amount <= 0:
            print("invalid amount")

        else:
            balance -= amount
            print(f" RS {amount} withdrawn successfully")
            print(f" your current  balance RS {balance}")

    elif choice == "3":
        amount = int(input("enter deposite amount: "))
        balance += amount
        print(f" your current balance RS {balance}")


    elif choice == "4":
        print(f"Thank you , visit again")
        break

    else:
        print("invalid choice")