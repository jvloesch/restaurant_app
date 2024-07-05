class Report():

    def __init__(self):
        self.total_orders_made = 0
        self.total_income = 0
        self.total_orders_delivered = 0

    def to_string(self):
        return "Total orders made: " + str(self.total_orders_made) + " | Total orders delivered: " + str(self.total_orders_delivered) + " | Total Income: $" + str(self.total_income)