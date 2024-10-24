import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QComboBox
from menuwindow import MenuWindow
from chef_window import ChefWindow
from cook_window import OrdersWindow


class AuthorizationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.role_label = QLabel("Роль")
        self.role_input = QComboBox()
        self.role_input.addItems(["Повар", "Су-Шеф", "Гость", "Шеф"])

        self.phone_label = QLabel("Телефон")
        self.phone_input = QLineEdit()
        self.password_label = QLabel("Пароль")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Логин")
        self.login_button.clicked.connect(self.authorize_user)

        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def authorize_user(self):
        role = self.role_input.currentText()
        phone = self.phone_input.text()
        password = self.password_input.text()

        if not role or not phone or not password:
            QMessageBox.warning(self, "Ошибка ввода", "Поля не заполнены")
            return

        try:
            with open("users.txt", "r") as file:
                users = file.readlines()
                for user in users:
                    user_details = user.strip().split(",")
                    if user_details[2] == phone and user_details[3] == password and user_details[4] == role:
                        # menuwindow
                        if user_details[4] == 'Гость':
                            self.menu_window = MenuWindow()
                            self.menu_window.show()
                        elif user_details[4] == 'Шеф':
                            self.chef_window = ChefWindow('orders.csv')
                            self.chef_window.show()
                        else:
                            self.order_window = OrdersWindow('orders.csv')
                            self.order_window.show()
                        return

                QMessageBox.warning(self, "Ошибка авторизации", "Неверные данные")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка!", f"Данные пользователя не могут быть считаны: {e}")
