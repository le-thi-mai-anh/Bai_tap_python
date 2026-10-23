import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class CuaSoDangNhap(QMainWindow):
    def __init__(self):
        super().__init__()

        # Lấy đường dẫn file UI trong thư mục Buoi_10
        dir_path = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(dir_path, 'form_dang_nhap.ui')

        # Nạp giao diện
        uic.loadUi(ui_path, self)

        # Bắt sự kiện khi bấm nút Đăng nhập
        self.nut_dang_nhap.clicked.connect(self.dang_nhap)

    def dang_nhap(self):
        tai_khoan = self.lineEdit.text()
        mat_khau = self.lineEdit_2.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(
                self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!"
            )
        else:
            QMessageBox.information(
                self, "Thông báo",
                "Đăng nhập thành công! Xin chào " + tai_khoan
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())