from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLabel, QGridLayout, \
    QRadioButton, QButtonGroup
from authorization import AuthorizationWindow
from registration import RegistrationWindow


class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное меню")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.auth_button = QPushButton("Авторизация")
        self.auth_button.clicked.connect(self.open_authorization)
        layout.addWidget(self.auth_button)

        self.reg_button = QPushButton("Регистрация")
        self.reg_button.clicked.connect(self.open_registration)
        layout.addWidget(self.reg_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_authorization(self):
        self.auth_window = AuthorizationWindow()
        self.auth_window.show()

    def open_registration(self):
        self.reg_window = RegistrationWindow()
        self.reg_window.show()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainMenuWindow()
    main_window.show()
    app.exec_()
