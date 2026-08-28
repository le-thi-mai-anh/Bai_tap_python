# Hoạt động 5: Mini project - Đăng ký thônng tin cá nhân
print ("[ Hoạt động 5: Mini project - Đăng ký thonng tin cá nhân ]")
# 1. Nhập dữ liệu đầu vào từ bàn phím
ho_ten = input("Nhap ho ten: ")
sdt = input("Nhap so dien thoai: ")
email = input("Nhap email: ")

# 2. Xử lý chuẩn hóa chuỗi và kiểm tra điều kiện dữ liệu cơ bản
ho_ten_chuan = " ".join(ho_ten.split()).title()
sdt_hop_le = len(sdt) == 10
email_hop_le = "@" in email

# 3. In kết quả kiểm tra ra màn hình (True/False)
print(f"Ho ten (da chuan hoa): {ho_ten_chuan}")
print(f"So dien thoai hop le (du 10 ky tu)? {sdt_hop_le}")
print(f"Email hop le (co ky tu @)? {email_hop_le}")
