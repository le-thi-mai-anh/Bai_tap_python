
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout


app = QApplication(sys.argv)

cua_so = QWidget()
cua_so.setWindowTitle("Vi du Grid Layout")

layout = QGridLayout()

layout.addWidget(QLabel("Tai khoan:"), 0, 0)
layout.addWidget(QLineEdit(), 0, 1)

layout.addWidget(QLabel("Mat khau:"), 1, 0)
layout.addWidget(QLineEdit(), 1, 1)

layout.addWidget(QPushButton("Dang nhap"), 2, 1)

cua_so.setLayout(layout)
cua_so.show()

sys.exit(app.exec_())
