
class OrdersList():

    def __init__(self, status):
        self.list_of_orders = []
        self.status = status

    def addOrder(self, order):
        self.list_of_orders.append(order)

    def printAllOrders(self):
        for order in self.list_of_orders:
            order.print_order()