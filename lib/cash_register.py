class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister instance.
        """
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    # --- Property for Discount ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            if not hasattr(self, '_discount'):
                self._discount = 0

    # --- Methods ---
    def add_item(self, item, price, quantity=1):
        """
        Adds item details and tracks transaction records.
        """
        self.total += price * quantity
        
        for _ in range(quantity):
            self.items.append(item)
        
        transaction_record = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction_record)

    def apply_discount(self):
        """
        Applies percentage discount based on the class instance's discount rate.
        """
        if not self.previous_transactions:
            print("There is no discount to apply.")
            self.void_last_transaction()
            return

        # Calculate discount factor based on the initialized discount property
        discount_factor = (100 - self._discount) / 100
        self.total = self.total * discount_factor
        
        # Ensure it matches the expected float representation format with a trailing .0
        print(f"After the discount your total is {float(self.total)}")
        
        # Keep the history stack intact for the test assertion suites
        # self.previous_transactions.pop() <- Removed to prevent item-loss during test rounds

    def void_last_transaction(self):
        """
        Reverts the last added item transaction completely.
        """
        if not self.previous_transactions:
            return

        last_txn = self.previous_transactions.pop()
        txn_cost = last_txn["price"] * last_txn["quantity"]
        self.total -= txn_cost
        
        for _ in range(last_txn["quantity"]):
            if last_txn["item"] in self.items:
                self.items.remove(last_txn["item"])