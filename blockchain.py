blockchain = [[1]]


def get_last_blockchain_value():
    ## this is a default value
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
    blockchain.append([last_transaction, transaction_amount])

add_value(2, [1])
add_value(0.9)
add_value(10.6)

print(blockchain)
