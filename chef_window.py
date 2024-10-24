import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton, QHBoxLayout, \
    QLabel, QMessageBox
from PyQt5.QtCore import Qt


def get_filtered_orders(csv_file):
    df = pd.read_csv(csv_file)
    filtered_df = df[df['Статус'] == 0]
    return df, filtered_df


def save_orders(csv_file, df):
    df.to_csv(csv_file, index=False)


class ChefWindow(QWidget):
    def __init__(self, csv_file):
        super().__init__()

        self.csv_file = csv_file
        self.df, self.orders = get_filtered_orders(csv_file)

        self.setWindowTitle('Orders')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.populate_list()

        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def populate_list(self):
        self.list_widget.clear()
        for index, row in self.orders.iterrows():
            order_widget = QWidget()
            order_layout = QHBoxLayout()

            order_details = (
                f"Дата: {row['date']}, "
                f"Зал: {row['hall']}, "
                f"Количество гостей: {row['number of guests']}, "
                f"Мероприятие: {row['type of event']}, "
                f"Меню: {row['menu']}, "
                f"Контактная информация: {row['contact info']}"
            )

            label = QLabel(order_details)
            label.setWordWrap(True)

            confirm_button = QPushButton("Подтвердить")
            confirm_button.clicked.connect(lambda _, idx=index: self.confirm_order(idx))

            order_layout.addWidget(label)
            order_layout.addWidget(confirm_button)
            order_widget.setLayout(order_layout)

            list_item = QListWidgetItem()
            list_item.setSizeHint(order_widget.sizeHint())

            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, order_widget)

    def confirm_order(self, index):
        self.df.at[index, 'Статус'] = 1
        save_orders(self.csv_file, self.df)
        QMessageBox.information(self, "Мероприятие подтверждено", f"Мероприятие {index} подтверждено")
        self.df, self.orders = get_filtered_orders(self.csv_file)
        self.populate_list()


