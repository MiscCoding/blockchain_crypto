blockchain = [[1]]

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([get_last_blockchain_value(), transaction_amount])

add_value(2)
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.09)
add_value(10.98, get_last_blockchain_value())

print(blockchain)
