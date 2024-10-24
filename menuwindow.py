import sys
import csv

import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QComboBox, QDateTimeEdit, QSpinBox, QGridLayout, QGroupBox, QCheckBox, QButtonGroup, QRadioButton
from PyQt5.QtCore import QDateTime

banquet_food = []
CoffeeBreak_food = []

class BanquetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Банкетное меню")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.dishes_label = QLabel("Выбрать блюда на банкет")
        layout.addWidget(self.dishes_label)

        self.dishes_layout = QGridLayout()

        self.add_dish_selection("Салаты", ["Цезарь", "Греческий", "Оливье"], 0)
        self.add_dish_selection("Горячие блюда", ["Бефстроганов", "Фрикассе из курицы", "Стейк лосося"], 1)
        self.add_dish_selection("Холодые закуски", ["Ассорти брускет", "Ассорти канапе", "Овощное плато"], 2)
        self.add_dish_selection("Горячие закуски", ["Жульен из курицы", "Жульен из языка", "Фаршированные грибы"], 3)
        self.add_dish_selection("Десерты", ["Анна Павлова", "Чизкейк", "Медовик"], 4)
        self.add_dish_selection("Напитки", ["Вино", "Сок", "Газированная вода"], 5)
        self.add_dish_selection("Закуски", ["Мясная тарелка", "Сырная тарелка", "Фруктовая тарелка"], 6)

        layout.addLayout(self.dishes_layout)

        self.submit_button = QPushButton("Подтвердить")
        self.submit_button.clicked.connect(self.submit_selection)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_dish_selection(self, category, dishes, row):
        category_label = QLabel(category)
        self.dishes_layout.addWidget(category_label, row, 0, 1, 2)

        for i, dish in enumerate(dishes):
            dish_label = QLabel(dish)
            quantity_spinbox = QSpinBox()
            quantity_spinbox.setRange(0, 100)
            self.dishes_layout.addWidget(dish_label, row, 2*i + 2)
            self.dishes_layout.addWidget(quantity_spinbox, row, 2*i + 3)
            setattr(self, f"{dish.lower().replace(' ', '_')}_spinbox", quantity_spinbox)

    def submit_selection(self):
        selected_dishes = {}

        # Collect selected dishes with quantities
        for dish in ["Цезарь", "Греческий", "Оливье", "Бефстроганов", "Фрикассе из курицы", "Стейк лосося",
                     "Ассорти брускет", "Ассорти канапе", "Овощное плато", "Жульен из курицы", "Жульен из языка",
                     "Фаршированные грибы", "Анна Павлова", "Чизкейк", "Медовик", "Вино", "Сок", "Газированная вода",
                     "Мясная тарелка", "Сырная тарелка", "Фруктовая тарелка"]:
            spinbox = getattr(self, f"{dish.lower().replace(' ', '_')}_spinbox")
            quantity = spinbox.value()
            if quantity > 0:
                selected_dishes[dish] = quantity

        global banquet_food
        banquet_food.append(selected_dishes)
        self.close()


class CoffeeBreakWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню для кофе-брейка")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        self.dishes_label = QLabel("Выбрать меню для кофе-брейка")
        layout.addWidget(self.dishes_label)

        self.dishes_layout = QGridLayout()

        self.add_dish_selection("Сэндвичи", ["Мясной сендвич", "Сырный сендвич", "Вегетерианский сендвич"], 0)
        self.add_dish_selection("Круассаны", ["Шоколадный круассан", "Миндальный круассан", "Сливочный круассан"], 1)
        self.add_dish_selection("Mини-сендвичи", ["Мясной мини-сендвич", "Сырный мини-сендвич", "Вегетерианский мини-сендвич"], 2)
        self.add_dish_selection("Канапе", ["Канапе с лососем", "Канапе с томатами", "Канапе с сыром"], 3)
        self.add_dish_selection("Напитки", ["Кола", "Сок"], 4)

        layout.addLayout(self.dishes_layout)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_selection)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_dish_selection(self, category, dishes, row):
        category_label = QLabel(category)
        self.dishes_layout.addWidget(category_label, row, 0, 1, 2)

        for i, dish in enumerate(dishes):
            dish_label = QLabel(dish)
            quantity_spinbox = QSpinBox()
            quantity_spinbox.setRange(0, 100)
            self.dishes_layout.addWidget(dish_label, row, 2*i + 2)
            self.dishes_layout.addWidget(quantity_spinbox, row, 2*i + 3)
            setattr(self, f"{dish.lower().replace(' ', '_')}_spinbox", quantity_spinbox)
            self.close()

    def submit_selection(self):
        selected_dishes = {}

        # Collect selected dishes with quantities
        for dish in ["Мясной сендвич", "Сырный сендвич", "Вегетерианский сендвич", "Шоколадный круассан",
                     "Миндальный круассан", "Сливочный круассан", "Мясной мини-сендвич", "Сырный мини-сендвич",
                     "Вегетерианский мини-сендвич", "Канапе с лососем", "Канапе с томатами", "Канапе с сыром", "Кола", "Сок"]:
            spinbox = getattr(self, f"{dish.lower().replace(' ', '_')}_spinbox")
            quantity = spinbox.value()
            if quantity > 0:
                selected_dishes[dish] = quantity

        global CoffeeBreak_food
        CoffeeBreak_food.append(selected_dishes)
        self.close()

"""
banquet_food = []


class BanquetWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Banquet Menu Selection")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()
        self.dishes_label = QLabel("Select Dishes for Banquet")
        layout.addWidget(self.dishes_label)

        self.dishes_layout = QGridLayout()

        self.add_dish_selection("Salads", ["Caesar", "Greek", "Garden"], 0)
        self.add_dish_selection("Hot Dishes", ["Steak", "Chicken", "Fish"], 1)
        self.add_dish_selection("Cold Appetizers", ["Bruschetta", "Deviled Eggs", "Cheese Platter"], 2)
        self.add_dish_selection("Hot Appetizers", ["Spring Rolls", "Mini Quiches", "Stuffed Mushrooms"], 3)
        self.add_dish_selection("Desserts", ["Chocolate Cake", "Cheesecake", "Fruit Salad"], 4)
        self.add_dish_selection("Drinks", ["Wine", "Juice", "Soda"], 5)
        self.add_dish_selection("General Snacks", ["Meat Platter", "Cheese Platter", "Fruit Platter"], 6)

        layout.addLayout(self.dishes_layout)

        # Add submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_selection)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_dish_selection(self, category, dishes, row):
        category_label = QLabel(category)
        self.dishes_layout.addWidget(category_label, row, 0)

        button_group = QButtonGroup(self)
        for i, dish in enumerate(dishes):
            radio_button = QRadioButton(dish)
            self.dishes_layout.addWidget(radio_button, row, i + 1)
            button_group.addButton(radio_button)

        setattr(self, f"{category.lower().replace(' ', '_')}_group", button_group)

    def submit_selection(self):
        selected_dishes = []

        # Collect selected dishes from each button group
        for category in ["salads", "hot_dishes", "cold_appetizers", "hot_appetizers", "desserts", "drinks",
                         "general_snacks"]:
            button_group = getattr(self, f"{category}_group")
            checked_button = button_group.checkedButton()
            if checked_button:
                selected_dishes.append(checked_button.text())

        # Add selected dishes to banquet_food list
        global banquet_food
        banquet_food.extend(selected_dishes)
        self.close()


CoffeeBreak_food = []


class CoffeeBreakWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Break Menu Selection")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.dishes_label = QLabel("Select Dishes for Coffee Break")
        layout.addWidget(self.dishes_label)

        self.dishes_layout = QGridLayout()

        self.add_dish_selection("Sandwiches", ["Ham Sandwich", "Cheese Sandwich", "Veggie Sandwich"], 0)
        self.add_dish_selection("Croissants", ["Chocolate Croissant", "Almond Croissant", "Butter Croissant"], 1)
        self.add_dish_selection("Mini Sandwiches", ["Mini Ham", "Mini Cheese", "Mini Veggie"], 2)
        self.add_dish_selection("Canapes", ["Salmon Canape", "Tomato Canape", "Cheese Canape"], 3)
        self.add_dish_selection("Drinks", ["Fruit Drink", "Juice"], 4)

        layout.addLayout(self.dishes_layout)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_selection)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_dish_selection(self, category, dishes, row):
        category_label = QLabel(category)
        self.dishes_layout.addWidget(category_label, row, 0)

        button_group = QButtonGroup(self)
        for i, dish in enumerate(dishes):
            radio_button = QRadioButton(dish)
            self.dishes_layout.addWidget(radio_button, row, i + 1)
            button_group.addButton(radio_button)

        setattr(self, f"{category.lower().replace(' ', '_')}_group", button_group)

    def submit_selection(self):
        selected_dishes = []

        # Collect selected dishes from each button group
        for category in ["sandwiches", "croissants", "mini_sandwiches", "canapes", "drinks"]:
            button_group = getattr(self, f"{category}_group")
            checked_button = button_group.checkedButton()
            if checked_button:
                selected_dishes.append(checked_button.text())

        global CoffeeBreak_food
        CoffeeBreak_food.extend(selected_dishes)

        self.close()
"""

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.datetime_label = QLabel("Дата")
        self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_input.setCalendarPopup(True)

        self.hall_label = QLabel("Зал")
        self.hall_input = QLineEdit()

        self.guests_label = QLabel("Количество гостей")
        self.guests_input = QSpinBox()
        self.guests_input.setRange(1, 500)

        self.event_type_label = QLabel("Тип мероприятия")
        self.banquet_button = QPushButton("Банкет")
        self.banquet_button.clicked.connect(self.open_banquet_window)
        self.coffee_break_button = QPushButton("Кофе-брейк")
        self.coffee_break_button.clicked.connect(self.open_coffee_break_window)

        self.contact_info_group_box = QGroupBox("Контактные данные")
        self.contact_info_layout = QGridLayout()
        self.populate_contact_info()

        self.submit_button = QPushButton("Подтвердить")
        self.submit_button.clicked.connect(self.submit_event)

        layout.addWidget(self.datetime_label)
        layout.addWidget(self.datetime_input)
        layout.addWidget(self.hall_label)
        layout.addWidget(self.hall_input)
        layout.addWidget(self.guests_label)
        layout.addWidget(self.guests_input)
        layout.addWidget(self.event_type_label)
        layout.addWidget(self.banquet_button)
        layout.addWidget(self.coffee_break_button)
        layout.addWidget(self.contact_info_group_box)
        layout.addWidget(self.submit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_banquet_window(self):
        self.banquet_window = BanquetWindow()
        self.banquet_window.show()

    def open_coffee_break_window(self):
        self.coffee_break_window = CoffeeBreakWindow()
        self.coffee_break_window.show()

    def populate_contact_info(self):
        self.first_name_label = QLabel("Имя")
        self.first_name_input = QLineEdit()
        self.last_name_label = QLabel("Фамилия")
        self.last_name_input = QLineEdit()
        self.phone_label = QLabel("Телефон")
        self.phone_input = QLineEdit()
        self.event_name_label = QLabel("Название мероприятия")
        self.event_name_input = QLineEdit()

        self.contact_info_layout.addWidget(self.first_name_label, 0, 0)
        self.contact_info_layout.addWidget(self.first_name_input, 0, 1)
        self.contact_info_layout.addWidget(self.last_name_label, 1, 0)
        self.contact_info_layout.addWidget(self.last_name_input, 1, 1)
        self.contact_info_layout.addWidget(self.phone_label, 2, 0)
        self.contact_info_layout.addWidget(self.phone_input, 2, 1)
        self.contact_info_layout.addWidget(self.event_name_label, 3, 0)
        self.contact_info_layout.addWidget(self.event_name_input, 3, 1)
        self.contact_info_group_box.setLayout(self.contact_info_layout)

    def submit_event(self):
        datetime = self.datetime_input.dateTime().toString()
        hall = self.hall_input.text()
        guests = self.guests_input.value()
        event_type = "Банкет" if self.banquet_window.isVisible() else "Кофе-брейк"

        contact_data = {
            "Имя": self.first_name_input.text(),
            "Фамилия": self.last_name_input.text(),
            "Номер телефона": self.phone_input.text(),
            "Название мероприятия": self.event_name_input.text()
        }

        try:
            orders = pd.read_csv('orders.csv')
            menu = []
            if len(banquet_food) > 0:
                menu = banquet_food
            else:
                menu = CoffeeBreak_food
            d = {"Дата": datetime, "Зал": hall, "Количество гостей": guests, "Вид мероприятия": event_type, "Меню": menu,
                 "Контактная информация": contact_data.values(), "Статус": 0}
            orders = pd.concat([orders, pd.DataFrame([d])], ignore_index=True)
            orders.to_csv('orders.csv', index=False, encoding='utf-8-sig')
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Информация о мероприятии не может быть сохранена: {e}")

        self.close()


    def clear_inputs(self):
        self.datetime_input.setDateTime(QDateTime.currentDateTime())
        self.hall_input.clear()
        self.guests_input.setValue(1)
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.phone_input.clear()
        self.event_name_input.clear()