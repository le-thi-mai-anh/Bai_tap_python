#Bài tập 3.1 – Kết nối QPushButton.clicked với slot hiển thị nội dung QLineEdit

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class CuaSo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hoat dong 3.1")
        self.nut_bam = QPushButton("Bam vao day")

        self.nut_bam.clicked.connect(self.xu_ly_nut_bam)

        bo_cuc = QVBoxLayout()
        bo_cuc.addWidget(self.nut_bam)
        self.setLayout(bo_cuc)

    def xu_ly_nut_bam(self):
        print("Ban vua bam nut!")


app = QApplication(sys.argv)
cua_so = CuaSo()
cua_so.show()
sys.exit(app.exec_())

#Hoạt động 3.2 – Thay đổi nội dung khi bấm nút

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class CuaSo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hoat dong 3.2")

        self.nhan = QLabel("Chua bam nut")
        self.nut_bam = QPushButton("Bam vao day")

        self.nut_bam.clicked.connect(self.cap_nhat_noi_dung)

        bo_cuc = QVBoxLayout()
        bo_cuc.addWidget(self.nhan)
        bo_cuc.addWidget(self.nut_bam)
        self.setLayout(bo_cuc)

    def cap_nhat_noi_dung(self):
        self.nhan.setText("Ban vua bam nut!")


app = QApplication(sys.argv)
cua_so = CuaSo()
cua_so.show()
sys.exit(app.exec_())
