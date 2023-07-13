def main():
    # This program will ask the user to enter their budget for the month.
    print('Welcome To Your Budget Tracker!')
    budget = float(input("Enter your budget for the month: "))
    total_transaction = 0
    all_transactions = []
    all_names = []
    remainder = 0

    # Initialize a for loop to iterate options to either enter a transaction or quit.
    while True:
        
        print_menu()
        
        command = input("Enter your choice: ")
        
        if command == "1":
            transaction = float(input("Enter the amount of the transaction: "))
            name = input("Enter the name of the transaction: ")
            total_transaction += float(transaction)
            remainder = budget - total_transaction
            
            all_transactions.append(transaction)
            all_names.append(name)
            
        if command == "2":
            print("Here is your transaction history:")
            print("------------------------------------")
            
            for (i, j) in zip(all_transactions, all_names):
                print(f'${i} for {j}')
            
            print("Total Transaction: " + str(total_transaction))
            print("------------------------------------")
                
        if command == "3":
            print("------------------------------------")
            print(f'You have ${budget - total_transaction} remaining.')
            print("------------------------------------")
            
        if command == "4":
            print("------------------------------------")
            print(f'You have spent a total of ${total_transaction}.')
            print(f'This month, you have ${remainder} remaining.')
            if remainder < 0:
                print("You have exceeded over your budget.")
            elif remainder > 0:
                print("You have money remaining from your budget.")
            elif remainder == 0:
                print("You have spent all of your budget.")
            print("------------------------------------")
        
        if command == "5":
            break

def print_menu():
    print('1. Enter a transaction')
    print('2. Show transactions history')
    print('3. Show remaining budget')
    print('4. Account Summary')
    print('5. Quit')


if __name__ == "__main__":
    main()
