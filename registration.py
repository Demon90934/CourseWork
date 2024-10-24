import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QMessageBox, QComboBox


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setGeometry(100, 100, 300, 250)

        layout = QVBoxLayout()

        self.name_label = QLabel("Имя")
        self.name_input = QLineEdit()
        self.surname_label = QLabel("Фамилия")
        self.surname_input = QLineEdit()
        self.phone_label = QLabel("Телефон")
        self.phone_input = QLineEdit()
        self.password_label = QLabel("Пароль")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.role_label = QLabel("Role")
        self.role_input = QComboBox()
        self.role_input.addItems(["Повар", "Су-Шеф", "Гость", "Шеф"])

        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.register_user)

        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.role_label)
        layout.addWidget(self.role_input)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def register_user(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        phone = self.phone_input.text()
        password = self.password_input.text()
        role = self.role_input.currentText()

        if not name or not surname or not phone or not password or not role:
            QMessageBox.warning(self, "Ошибка ввода", "Поля не заполнены")
            return

        user_data = f"{name},{surname},{phone},{password},{role}\n"

        try:
            with open("users.txt", "a") as file:
                file.write(user_data)
            QMessageBox.information(self, "Успешно!", "Пользователь зарегистрирован")
            self.clear_inputs()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Данные пользователя не могут быть сохранены: {e}")

    def clear_inputs(self):
        self.name_input.clear()
        self.surname_input.clear()
        self.phone_input.clear()
        self.password_input.clear()
        self.role_input.setCurrentIndex(0)

