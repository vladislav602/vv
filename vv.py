import random

from PyQt5.QtWidgets import *

app = QApplication|([])

window = QWidget()


winner_lbl = QLabel("Переможець")
generate_winner_btn_QPushuButton("Щтримати переможтця")


window.show()

def winner_func():
    num = random.randint(1,4)
    winner_lbl.setText("Переможець" + str(num))