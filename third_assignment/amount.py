class Amount:
    def __init__(self, amount, timestamp, transaction_type):
        self.amount = amount
        self.timestamp = timestamp
        self.transaction_type = transaction_type


    def __repr__(self):
        return f"Amount({self.amount}, {self.timestamp}, {self.transaction_type})"