
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class CuaSo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hoat dong 1 - PyQt5")
        self.resize(400, 300)

        nhan = QLabel("Xin chao PyQt5!")

        layout = QVBoxLayout()
        layout.addWidget(nhan)
        self.setLayout(layout)


app = QApplication(sys.argv)
cua_so = CuaSo()
cua_so.show()
sys.exit(app.exec_())

