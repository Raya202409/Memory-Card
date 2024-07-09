#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QButtonGroup)
from random import *

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Татарстана','Татарский','Башкирский','Татарстанский','Булгарский'))
question_list.append(Question('Какой группы не существует в k-pop?','pinkblack','Twice','TXT','(G)I-dle'))
question_list.append(Question('Какой из этих брендов косметики корейский?','2aN','pupa','clorins','Dolce&Gabanna'))
question_list.append(Question('Кем не является Чэн Сяо?','модель','певица','танцовщица','актриса'))
question_list.append(Question('Какая столица Бразилии?','Бразилиа','Рио-де-Жанейро','Сан-Паулу','Салвадор'))
question_list.append(Question('В каком году родился Александр Сергеевич Пушкин?','1799','1800','1837','1820'))
question_list.append(Question('Джису(blackpink) - "Королева ..."','Dior','Chanel','LOUIS VUITTON','Cartier'))
question_list.append(Question('Песня на татарском из сериала "Слово пацана"','Пыяла','Аяла','Аигел','Мехеббет'))
question_list.append(Question('Какая российская песня сильно завирусилась этой зимой среди иностранцев?','Катя Лель "Мой мармеладный"','группа "Комбинация" "Аmerican Boy"','группа "Мираж" "Музыка нас связала"','Женя Любич "Russian Girl"'))                                                    
question_list.append(Question('Сколько сезонов в сериале "Учитель Ким: Доктор романтик"','3 сезона','2 сезона','5 сезонов','4 сезона'))

app = QApplication([])

btn_OK = QPushButton('Ответить')
Ib_Question = QLabel('Самый сложный вопрос')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
Ib_result = QLabel('прав ты или нет?')
Ib_correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(Ib_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(Ib_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    Ib_Question.setText(q.question)
    Ib_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    Ib_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:',window.total,'\n-Правильных ответов:',window.score)
        print('Рейтинг:',(window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:',(window.score/window.total*100),'%')

def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:',window.total,'\n-Правильных ответов:',window.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
window = QWidget()    
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
#'Государственный язык Татарстана','Татарский','Башкирский','Татарстанский','Булгарский'


btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec()