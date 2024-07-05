class Order():
    previous_order = 0

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products
        self.order_number = Order.previous_order+1
        Order.previous_order += 1
        self.total_price = self.calculateTotalPrice()
    
    def calculateTotalPrice(self):
        total_price = 0
        for product in self.list_of_products:
             total_price += product.price
        return total_price