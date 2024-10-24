import pandas as pd

d = {"Дата": '25.09', "Зал": 'N', "Количество гостей": 1, "Вид мероприятия": 'T', "Меню": ['apple'],
     "Контактная информация": ['a'], "Статус": 2}
df = pd.DataFrame(data=d)
df.to_csv('C:/Users/geyle/PycharmProjects/pythonProject9/orders.csv')
