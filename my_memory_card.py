#создай приложение для запоминания информации
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import *
from random import *

#класс
class Question():
    def __init__(self, question, right_otv, bad1, bad2, bad3):
        self.question = question
        self.right_otv = right_otv
        self.bad1 = bad1
        self.bad2 = bad2
        self.bad3 = bad3

#функции
def ask(qclass: Question):
    shuffle(answer)
    q.setText(qclass.question)
    answer[0].setText(qclass.right_otv)
    answer[1].setText(qclass.bad1)
    answer[2].setText(qclass.bad2)
    answer[3].setText(qclass.bad3)

def showwww():
    RadioGB.hide()
    Grupp_text.show()

    if answer[0].isChecked():
        t1.setText('Верно')
        t2.setText('Молодец!')
        win.score += 1
    else:
        t1.setText('Неверно')
        t2.setText('Следует изучить вопрос лучше')
    butt.setText('дальше')


def next_q():
    Grupp_text.hide()
    RadioGB.show()

    numb = randint(0, len(q_list) - 1)
    Rgb.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    Rgb.setExclusive(True) 

    print('Статистика')
    print('-Всего вопросов:', win.total)
    print('-Правильных ответов:', win.score)
    j = win.score / win.total * 100
    win.total += 1
    print('Рейтинг:', j)
    lad = q_list[numb]
    ask(lad)
    q_list.remove(lad)

    butt.setText('ответить')

def click_OK(qclass: Question):
    if butt.text() == 'дальше':
        next_q()
    else:
        showwww()
#создание элементов интерфейса
app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс от Crazy People')
win.resize(400, 500)
win.score = 0
win.total = 1
#создание виджетов главного окна
q = QLabel('Какой национальности не существует?')
RadioGB = QGroupBox('Варианты ответа')
a1 = QRadioButton('Смурфы')
a2 = QRadioButton('Энцы')
a3 = QRadioButton('Чулымцы')
a4 = QRadioButton('Алеуты')
butt = QPushButton('Ответить')

Rgb = QButtonGroup()
Rgb.addButton(a1)
Rgb.addButton(a2)
Rgb.addButton(a3)
Rgb.addButton(a4)

answer = [a1, a2, a3, a4]
#расположение виджетов по лэйаутам
len6 = QVBoxLayout()
len4 = QHBoxLayout()
len1 = QVBoxLayout()
len2 = QHBoxLayout()
len3 = QHBoxLayout()
len5 = QHBoxLayout()
len7 = QVBoxLayout()

Grupp_text = QGroupBox('Результат теста')
t1 = QLabel('Правильно/Неправильно')
t2 = QLabel('Правильный ответ')
# Группа 1
len2.addWidget(a1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len2.addWidget(a2, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len3.addWidget(a3, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len3.addWidget(a4, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len1.addLayout(len2)
len1.addLayout(len3)

RadioGB.setLayout(len1)
# группа 2 
len7.addWidget(t1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len7.addWidget(t2, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

Grupp_text.setLayout(len7)
# Форма
len4.addWidget(q, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
len5.addWidget(butt, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

len6.addLayout(len4)
len6.addWidget(RadioGB)
len6.addWidget(Grupp_text)
len6.addLayout(len5)
# Главная форма
Grupp_text.hide()
win.setLayout(len6)
#
q2 = Question('2 + 2', '4', '5', '6', '1')
q3 = Question('4 * 3', '12', '6', '8', '11')
q4 = Question('20 / 4', '5', '7', '6', '8')
q5 = Question('11 * 54', '594', '564', '600', '449')

q_list = [q2, q3, q4, q5]
#кнопа
butt.clicked.connect(click_OK)
win.show()
app.exec()