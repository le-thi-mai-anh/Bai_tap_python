
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QComboBox, QPushButton,
    QVBoxLayout, QMessageBox
)


class FormThongTin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Thong tin ca nhan")
        self.setGeometry(300, 200, 350, 250)

        self.nhan_ten = QLabel("Nhap ho ten:")
        self.o_nhap_ten = QLineEdit()

        self.nhan_thanh_pho = QLabel("Chon thanh pho:")
        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems([
            "Ha Noi",
            "Da Nang",
            "TP.HCM",
            "Hue"
        ])

        self.nut_xac_nhan = QPushButton("Xac nhan")
        self.nhan_ket_qua = QLabel("")

        bo_cuc = QVBoxLayout()
        bo_cuc.addWidget(self.nhan_ten)
        bo_cuc.addWidget(self.o_nhap_ten)
        bo_cuc.addWidget(self.nhan_thanh_pho)
        bo_cuc.addWidget(self.chon_thanh_pho)
        bo_cuc.addWidget(self.nut_xac_nhan)
        bo_cuc.addWidget(self.nhan_ket_qua)

        self.setLayout(bo_cuc)

        self.nut_xac_nhan.clicked.connect(
            self.xu_ly_xac_nhan
        )

    def xu_ly_xac_nhan(self):
        ho_ten = self.o_nhap_ten.text()

        if ho_ten == "":
            QMessageBox.warning(
                self, "Thong bao",
                "Vui long nhap ho ten!"
            )
        else:
            thanh_pho = self.chon_thanh_pho.currentText()
            self.nhan_ket_qua.setText(
                f"Xin chao {ho_ten} den tu {thanh_pho}!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = FormThongTin()
    cua_so.show()
    sys.exit(app.exec_())
