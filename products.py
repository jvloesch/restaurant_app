
###### PRODUCT PARENT CLASS ###### 
class Product():
    def __init__(self):
        self.product_name = "Empty Product"
        self.price = 0

    def __str__(self):
        return '{}, ${}'.format(self.product_name, self.price)

###### STARTERS CHILD CLASSES ###### 
class FrenchFries(Product):
    def __init__(self, addition_of_sault):
        super().__init__()
        self.product_name = "French Fries"
        self.price = 5.0
        if(addition_of_sault):
            self.addition_of_sault = "Yes"
        else:
            self.addition_of_sault = "No"

    def __str__(self):
        return '{}, ${}, Addition of Sault: {}'.format(self.product_name, self.price, self.addition_of_sault)

class OnionRings(Product):
    def __init__(self):
        super().__init__()
        self.product_name = "Onion Rings"
        self.price = 6.0

class RoastedTomatoes(Product):
    def __init__(self, addition_of_sault):
        super().__init__()
        self.product_name = "Roasted Tomatoes"
        self.price = 4.0
        if(addition_of_sault):
            self.addition_of_sault = "Yes"
        else:
            self.addition_of_sault = "No"

    def __str__(self):
        return '{}, ${}, Addition of Sault: {}'.format(self.product_name, self.price, self.addition_of_sault)

###### MAIN DISHES CHILD CLASSES ###### 
class ItalianPasta(Product):
    def __init__(self):
        super().__init__()
        self.product_name = "Italian Pasta"
        self.price = 25.0

class Hamburguer(Product):
    def __init__(self, point_index):
        super().__init__()
        self.product_name = "Hamburguer"
        self.price = 30.0
        self.meat_point = self.setMeatPoint(point_index)

    def setMeatPoint(self, point_index):
        match point_index:
            case 1:
                return "Rare"
            case 2:
                return "Medium"
            case 3:
                return "Done"
            case _:
                return "Medium"
                
    def __str__(self):
        return '{}, ${}, Meat Point: {}'.format(self.product_name, self.price, self.meat_point)

class BrazilianClassicMeal(Product):
    def __init__(self, include_salad):
        self.product_name = "Brazilian Classic Meal"
        self.price = 23.0
        self.include_salad = include_salad
        if(include_salad):
            self.include_salad = "Yes"
        else:
            self.include_salad = "No"

    def __str__(self):
        return '{}, ${}, Salad Included: {}'.format(self.product_name, self.price, self.include_salad)

class SaladBowl(Product):
    def __init__(self):
        self.product_name = "Salad Bowl"
        self.price = 15.0

###### DRINKS CHILD CLASSES ###### 
class Water(Product):
    def __init__(self):
        self.product_name = "Water"
        self.price = 2.0

class Soda(Product):
    def __init__(self, sugar_free):
        self.product_name = "Soda"
        self.price = 3.5
        if(sugar_free):
            self.sugar_free = "Yes"
        else:
            self.sugar_free = "No"

    def __str__(self):
        return '{}, ${}, Sugar Free: {}'.format(self.product_name, self.price, self.sugar_free)

class Juice(Product):
    def __init__(self, addition_of_sugar):
        self.product_name = "Juice"
        self.price = 3.0
        if(addition_of_sugar):
            self.addition_of_sugar = "Yes"
        else:
            self.addition_of_sugar = "No"

    def __str__(self):
        return '{}, ${}, Addition of Sugar: {}'.format(self.product_name, self.price, self.addition_of_sugar)

class Beer(Product):
    def __init__(self):
        self.product_name = "Beer"
        self.price = 4.0

###### DESSERTS CHILD CLASSES ###### 
class IceCream(Product):
    def __init__(self, flavour_index):
        self.product_name = "Ice Cream"
        self.price = 7.0
        self.flavour = self.setMeatPoint(flavour_index)

    def setMeatPoint(self, flavour_index):
        match flavour_index:
            case 1:
                return "Chocolate"
            case 2:
                return "Strawberry"
            case _:
                return "Chocolate"
                
    def __str__(self):
        return '{}, ${}, Flavour: {}'.format(self.product_name, self.price, self.flavour)

class Donut(Product):
    def __init__(self):
        self.product_name = "Donut"
        self.price = 4.0

class Cheesecake(Product):
    def __init__(self):
        self.product_name = "Cheesecake"
        self.price = 5.0