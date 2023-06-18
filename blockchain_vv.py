blockchain = []


def get_last_blockchain_value():
    # this is a default value
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input("Your transaction amount please: "))
# This code helps reduce repetitive tasks with leaner code
#Global variable (not inside a function) can be used anywhere
#Local variable (inside a function) can only be used within function


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value() )

print(blockchain)
