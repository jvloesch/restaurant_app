from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLCDNumber, QSpinBox, QComboBox, QCheckBox, QPushButton, QMessageBox, QLineEdit
from PySide6.QtUiTools import QUiLoader
from products import Product, FrenchFries, OnionRings, RoastedTomatoes, ItalianPasta, Hamburguer, BrazilianClassicMeal, SaladBowl, Water, Soda, Juice, Beer, IceCream, Donut, Cheesecake
from order import Order
from report import Report
from orders_list import OrdersList
loader = QUiLoader()

ordered_products = OrdersList("Ordered")
preparation_products = OrdersList("Preparation")
delivered_products = OrdersList("Delivered")
daily_report = Report()


###### MAIN WINDOW ######

class MainWindow(QtCore.QObject):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = loader.load("main_window.ui", None)
        self.ui.setWindowTitle("Restaurant Manager")
        
        #Menu Triggers
        self.ui.quit.triggered.connect(self.quitApp)
        self.ui.show_menu.triggered.connect(self.showMenu)
        self.ui.show_kitchen.triggered.connect(self.showKitchen)
        self.ui.new_order.triggered.connect(self.showNewOrder)
        self.ui.delete_order.triggered.connect(self.showDeleteOrder)
        self.ui.update_order_status.triggered.connect(self.showUpdateOrder)
        self.ui.show_order_status.triggered.connect(self.showOrderStatus)
        self.ui.show_todays_reports.triggered.connect(self.showTodaysReports)
        self.ui.about_button.triggered.connect(self.showAbout)

    #Widget-Change Functions
    def show(self):
        self.ui.show()

    def quitApp(self):
        self.app.quit()

    def showMenu(self):
        menu_widget = MenuWidget()
        self.ui.setCentralWidget(menu_widget)

    def showKitchen(self):
        kitchen_widget = KitchenWidget()
        self.ui.setCentralWidget(kitchen_widget)

    def showNewOrder(self):
        new_order = NewOrder()
        self.ui.setCentralWidget(new_order)

    def showDeleteOrder(self):
        delete_order = DeleteOrder()
        self.ui.setCentralWidget(delete_order)

    def showUpdateOrder(self):
        update_order = UpdateOrder()
        self.ui.setCentralWidget(update_order)

    def showOrderStatus(self):
        order_status = ShowStatus()
        self.ui.setCentralWidget(order_status)
    
    def showTodaysReports(self):
        todays_report = ReportsWidget()
        self.ui.setCentralWidget(todays_report)

    def showAbout(self):
        about = AboutWidget()
        self.ui.setCentralWidget(about)

###### MAIN WINDOW CENTRAL WIDGETS ###### 

class MenuWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = loader.load("menu.ui", None)
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)
    
class ReportsWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        daily_report.total_orders_delivered = len(delivered_products.list_of_orders)
        report_str = str(daily_report.to_string())
        ret = QMessageBox.information(self, "Today's Report", report_str, QMessageBox.Ok)

class AboutWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        ret = QMessageBox.information(self, "About", "This app was developed by João Vítor Loesch as part of his first GUI development project in college.", QMessageBox.Ok)

class KitchenWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = loader.load("kitchen.ui", None)
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

        self.lcd1 = self.ui.findChild(QLCDNumber, "currentOrder")
        self.lcd2 = self.ui.findChild(QLCDNumber, "nextOrder1")
        self.lcd3 = self.ui.findChild(QLCDNumber, "nextOrder2")
        self.lcd4 = self.ui.findChild(QLCDNumber, "nextOrder3")
        self.lcd5 = self.ui.findChild(QLCDNumber, "nextOrder4")

        try:
            self.lcd1.display(self.displayOrder(0))
        except IndexError:
            pass
        try:
            self.lcd2.display(self.displayOrder(1))
        except IndexError:
            pass
        try:
            self.lcd3.display(self.displayOrder(2))
        except IndexError:
            pass
        try:
            self.lcd4.display(self.displayOrder(3))
        except IndexError:
            pass
        try:
            self.lcd5.display(self.displayOrder(4))
        except IndexError:
            pass

    def displayOrder(self, index):
        return preparation_products.list_of_orders[index].order_number

class NewOrder(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = loader.load("new_order.ui", None)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.setLayout(layout)
        self.list_of_products = []
        self.total_price = 0

        self.ui.send_order_button.clicked.connect(self.createOrder)
        self.ui.reset_button.clicked.connect(self.resetOrder)

        #Get Spin Boxes
        self.qntFrenchFries = self.ui.findChild(QSpinBox, "qntFrenchFries")
        self.qntOnionRings = self.ui.findChild(QSpinBox, "qntOnionRings")
        self.qntRoastedTomatoes = self.ui.findChild(QSpinBox, "qntRoastedTomatoes")
        self.qntItalianPasta = self.ui.findChild(QSpinBox, "qntItalianPasta")
        self.qntHamburguer = self.ui.findChild(QSpinBox, "qntHamburguer")
        self.qntBrazilianClassicMeal = self.ui.findChild(QSpinBox, "qntBrazilianClassicMeal")
        self.qntSaladBowl = self.ui.findChild(QSpinBox, "qntSaladBowl")
        self.qntWater = self.ui.findChild(QSpinBox, "qntWater")
        self.qntSoda = self.ui.findChild(QSpinBox, "qntSoda")
        self.qntJuice = self.ui.findChild(QSpinBox, "qntJuice")
        self.qntBeer = self.ui.findChild(QSpinBox, "qntBeer")
        self.qntIceCream = self.ui.findChild(QSpinBox, "qntIceCream")
        self.qntDonut = self.ui.findChild(QSpinBox, "qntDonut")
        self.qntCheesecake = self.ui.findChild(QSpinBox, "qntCheesecake")

        #Get Check Boxes
        self.french_fries_addition_of_sault = self.ui.findChild(QCheckBox, "french_fries_addition_of_sault")
        self.roasted_tomatoes_addition_of_sault = self.ui.findChild(QCheckBox, "roasted_tomatoes_addition_of_sault")
        self.rare_point = self.ui.findChild(QCheckBox, "rare_point")
        self.medium_point = self.ui.findChild(QCheckBox, "medium_point")
        self.done_point = self.ui.findChild(QCheckBox, "done_point")
        self.sugar_free = self.ui.findChild(QCheckBox, "sugar_free")
        self.include_salad = self.ui.findChild(QCheckBox, "include_salad")
        self.addition_of_sugar = self.ui.findChild(QCheckBox, "addition_of_sugar")
        self.chocolate_flavour = self.ui.findChild(QCheckBox, "chocolate_flavour")
        self.strawberry_flavour = self.ui.findChild(QCheckBox, "strawberry_flavour")

        #Checking Changes in Values and Updating Values

    #Create Order
    def createOrder(self):
        preparation_products.addOrder(self.createOrderObject())
        daily_report.total_orders_made += 1
        daily_report.total_income += self.total_price
        self.send_order_button_clicked()
        self.resetOrder()
        
    def send_order_button_clicked(self):
        ret = QMessageBox.information(self, "Order Confirmation", "The order has been successfully created. Total Price: $" +str(self.total_price), QMessageBox.Ok)

    def createOrderObject(self):
        #French Fries
        if(self.qntFrenchFries.value() > 0):
            for i in range(self.qntFrenchFries.value()):
                self.list_of_products.append(self.createFrenchFriesObject())
            
        #Onion Rings
        if(self.qntOnionRings.value() > 0):
            for i in range(self.qntOnionRings.value()):
                self.list_of_products.append(self.createOnionRingsObject())

        #Roasted Tomatoes
        if(self.qntRoastedTomatoes.value() > 0):
            for i in range(self.qntRoastedTomatoes.value()):
                self.list_of_products.append(self.creatRoastedTomatoesObject())

        #Italian Pasta
        if(self.qntItalianPasta.value() > 0):
            for i in range(self.qntItalianPasta.value()):
                self.list_of_products.append(self.createItalianPastaObject())

        #Hamburguer
        if(self.qntHamburguer.value() > 0):
            for i in range(self.qntHamburguer.value()):
                self.list_of_products.append(self.createHamburguerObject())

        #Brazilian Classic Meal
        if(self.qntBrazilianClassicMeal.value() > 0):
            for i in range(self.qntBrazilianClassicMeal.value()):
                self.list_of_products.append(self.createBrazilianClassicMealObject())

        #Salad Bowl
        if(self.qntSaladBowl.value() > 0):
            for i in range(self.qntSaladBowl.value()):
                self.list_of_products.append(self.createSaladBowlObject())

        #Water
        if(self.qntWater.value() > 0):
            for i in range(self.qntWater.value()):
                self.list_of_products.append(self.createWaterObject())

        #Soda
        if(self.qntSoda.value() > 0):
            for i in range(self.qntSoda.value()):
                self.list_of_products.append(self.createSodaObject())

        #Juice
        if(self.qntJuice.value() > 0):
            for i in range(self.qntJuice.value()):
                self.list_of_products.append(self.createJuiceObject())

        #Beer
        if(self.qntBeer.value() > 0):
            for i in range(self.qntBeer.value()):
                self.list_of_products.append(self.createBeerObject())

        #Ice Cream
        if(self.qntIceCream.value() > 0):
            for i in range(self.qntIceCream.value()):
                self.list_of_products.append(self.createIceCreamObject())

        #Donut
        if(self.qntDonut.value() > 0):
            for i in range(self.qntDonut.value()):
                self.list_of_products.append(self.createDonutObject())

        #Cheesecake
        if(self.qntCheesecake.value() > 0):
            for i in range(self.qntCheesecake.value()):
                self.list_of_products.append(self.createChessecakeObject())

        for product in self.list_of_products:
            self.total_price += product.price
        created_order = Order(self.list_of_products)
        created_order.status = "Preparation"
        return created_order


    #Reset Order
    def resetOrder(self):
        self.qntFrenchFries.setValue(0)
        self.qntOnionRings.setValue(0)
        self.qntRoastedTomatoes.setValue(0)
        self.qntItalianPasta.setValue(0)
        self.qntHamburguer.setValue(0)
        self.qntBrazilianClassicMeal.setValue(0)
        self.qntSaladBowl.setValue(0)
        self.qntWater.setValue(0)
        self.qntSoda.setValue(0)
        self.qntJuice.setValue(0)
        self.qntBeer.setValue(0)
        self.qntIceCream.setValue(0)
        self.qntDonut.setValue(0)
        self.qntCheesecake.setValue(0)
        self.french_fries_addition_of_sault.setChecked(0)
        self.roasted_tomatoes_addition_of_sault.setChecked(0)
        self.rare_point.setChecked(0)
        self.medium_point.setChecked(0)
        self.done_point.setChecked(0)
        self.include_salad.setChecked(0)
        self.sugar_free.setChecked(0)
        self.addition_of_sugar.setChecked(0)
        self.chocolate_flavour.setChecked(0)
        self.strawberry_flavour.setChecked(0)
        self.list_of_products = []
        self.total_price = 0
        

    #Create Products Objects for the Order
    def createFrenchFriesObject(self):
        if(self.french_fries_addition_of_sault.isChecked()):
            return FrenchFries(1)
        else:
            return FrenchFries(0)
        
    def createOnionRingsObject(self):
        return OnionRings()
    
    def creatRoastedTomatoesObject(self):
        if(self.roasted_tomatoes_addition_of_sault.isChecked()):
            return FrenchFries(1)
        else:
            return FrenchFries(0)
        
    def createItalianPastaObject(self):
        return ItalianPasta()
    
    def createHamburguerObject(self):
        if(self.medium_point.isChecked()):
            return Hamburguer(2) #Medium Point (default)
        elif(self.rare_point.isChecked()):
            return Hamburguer(1) #Rare Point
        elif(self.done_point.isChecked()):
            return Hamburguer(3) #Done Point
        else:
            return Hamburguer(2) #Medium Point
        
    def createBrazilianClassicMealObject(self):
        if(self.include_salad.isChecked()):
            return BrazilianClassicMeal(1)
        else:
            return BrazilianClassicMeal(0)
        
    def createSaladBowlObject(self):
        return SaladBowl() 
    
    def createWaterObject(self):
        return Water()
    
    def createSodaObject(self):
        if(self.sugar_free.isChecked()):
            return Soda(1)
        else:
            return Soda(0)
        
    def createJuiceObject(self):
        if(self.addition_of_sugar.isChecked()):
            return Juice(1)
        else:
            return Juice(0)
        
    def createBeerObject(self):
        return Beer()
    
    def createIceCreamObject(self):
        if(self.chocolate_flavour.isChecked()):
            return IceCream(1) #Chocolate (default)
        elif(self.strawberry_flavour.isChecked()):
            return IceCream(2) #Strawberry
        else:
            return IceCream(1) #Strawberry
        
    def createDonutObject(self):
        return Donut()
    
    def createChessecakeObject(self):
        return Cheesecake()
    

class DeleteOrder(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = loader.load("delete_order.ui", None)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.setLayout(layout)

        self.delete_order_button = self.ui.findChild(QPushButton, "delete_order_number")
        self.cancel_deletion_button = self.ui.findChild(QPushButton, "cancel_deletion_button")
        self.delete_order_number = self.ui.findChild(QSpinBox, "delete_order_number")

        self.ui.delete_order_button.clicked.connect(self.deleteOrder)
        self.ui.cancel_deletion_button.clicked.connect(self.cancelDeletion)

    def deleteOrder(self):
        order_found = False
        order_number_informed = self.delete_order_number.value()

        for order in ordered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                ordered_products.list_of_orders.pop(ordered_products.list_of_orders.index(order))
                order_found = True

        for order in preparation_products.list_of_orders:
            if(order.order_number == order_number_informed):
                preparation_products.list_of_orders.pop(preparation_products.list_of_orders.index(order))
                order_found = True

        for order in delivered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                delivered_products.list_of_orders.pop(delivered_products.list_of_orders.index(order))
                order_found = True

        if(order_found):
            self.deleted_order_message()
        else:
            self.order_not_found()
        self.delete_order_number.setValue(0)


    def deleted_order_message(self):
        ret = QMessageBox.information(self, "Deletion Confirmation", "The order has been successfully deleted", QMessageBox.Ok)

    def order_not_found(self):
        ret = QMessageBox.critical(self, "Deletion Error", "ERROR! Order number not found.", QMessageBox.Ok)

    def cancelDeletion(self):
        self.delete_order_number.setValue(0)
        

class UpdateOrder(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = loader.load("update_order.ui", None)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.selected_status = ""

        self.update_order_button = self.ui.findChild(QPushButton, "update_order_button")
        self.cancel_update_button = self.ui.findChild(QPushButton, "cancel_update_button")
        self.update_order_number = self.ui.findChild(QSpinBox, "update_order_number")
        self.status_combo_box = self.ui.findChild(QComboBox, "status_combo_box")

        self.ui.update_order_button.clicked.connect(self.updateOrder)
        self.ui.cancel_update_button.clicked.connect(self.cancelUpdate)
        self.ui.status_combo_box.activated.connect(self.updateChoice)

    def updateChoice(self):
        self.selected_status = self.status_combo_box.currentText()

    def updateOrdersList(self, order, new_status):
        temporary_order = order
        if(new_status == "Ordered"):
            ordered_products.list_of_orders.append(temporary_order)
        elif(new_status == "Preparation"):
            preparation_products.list_of_orders.append(temporary_order)
        else:
            delivered_products.list_of_orders.append(temporary_order)

    def updateOrder(self):
        order_found = False
        order_number_informed = self.update_order_number.value()

        for order in ordered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.updateOrdersList(order, self.selected_status)
                ordered_products.list_of_orders.pop(ordered_products.list_of_orders.index(order))
                order_found = True

        for order in preparation_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.updateOrdersList(order, self.selected_status)
                preparation_products.list_of_orders.pop(preparation_products.list_of_orders.index(order))
                order_found = True

        for order in delivered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.updateOrdersList(order, self.selected_status)
                delivered_products.list_of_orders.pop(delivered_products.list_of_orders.index(order))
                order_found = True

        if(order_found):
            self.found_order_message()
        else:
            self.order_not_found()
        self.update_order_number.setValue(0)


    def found_order_message(self):
        ret = QMessageBox.information(self, "Update Confirmation", "The order status has been update. New status is: " + self.selected_status, QMessageBox.Ok)

    def order_not_found(self):
        ret = QMessageBox.critical(self, "Search Error", "ERROR! Order number not found.", QMessageBox.Ok)

    def cancelUpdate(self):
        self.update_order_number.setValue(0)
        self.status_combo_box.setCurrentIndex(0)
        

class ShowStatus(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = loader.load("show_order_status.ui", None)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        self.setLayout(layout)
        self.setLayout(layout)
        self.status = ""
        self.found_order_object = ""

        self.search_order_button = self.ui.findChild(QPushButton, "search_order_button")
        self.cancel_search_button = self.ui.findChild(QPushButton, "cancel_search_button")
        self.search_order_number = self.ui.findChild(QSpinBox, "search_order_number")

        self.ui.search_order_button.clicked.connect(self.searchOrder)
        self.ui.cancel_search_button.clicked.connect(self.cancelSearch)

    def searchOrder(self):
        order_found = False
        
        order_number_informed = self.search_order_number.value()

        for order in ordered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.status = "Ordered"
                self.found_order_object = order
                order_found = True

        for order in preparation_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.status = "Preparation"
                self.found_order_object = order
                order_found = True

        for order in delivered_products.list_of_orders:
            if(order.order_number == order_number_informed):
                self.status = "Delivered"
                self.found_order_object = order
                order_found = True

        if(order_found):
            self.found_order_message()
        else:
            self.order_not_found()
        self.search_order_number.setValue(0)


    def print_order_objects(self, order):
        order.return_order()

    def found_order_message(self):
        ret = QMessageBox.information(self, "Search Completion", "The order status is: " + self.status, QMessageBox.Ok)

    def order_not_found(self):
        ret = QMessageBox.critical(self, "Search Error", "ERROR! Order number not found.", QMessageBox.Ok)

    def cancelSearch(self):
        self.search_order_number.setValue(0)
        
