class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    drink_machine = VendingMachine()

    # TODO: Purchase first input number of bottles of drinks
    drinks_to_buy1 = int(input())
    # TODO: Restock second input number of bottles of drinks
    bottles_to_stock = int(input())

    # TODO: Purchase last input number of bottles of drinks
    drinks_to_buy2 = int(input())

    # TODO: Report inventory
    drink_machine.purchase(drinks_to_buy1)
    drink_machine.restock(bottles_to_stock)
    drink_machine.purchase(drinks_to_buy2)
    drink_machine.report()