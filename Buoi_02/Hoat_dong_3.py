# Hoạt động 3:Number-int,float,..

# Bài 3.1: các kiểu số & chuyển đổi
print("[các kiểu số & chuyển đổi]")
# Khai báo các kiểu số
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

# In ra kiểu dữ liệu và thực hiện ép kiểu
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))  # ep int -> float
print(int(so_thuc))      # ep float -> int (cat phan thap phan)


# Bài 3.2: hàm built xử lý số
print("[ hàm built in xử lý số]")
# Khai báo các biến số
a = -7
b = 2.6789
c, d = 17, 5

# Thực thi các hàm built-in xử lý số và in kết quả
print(abs(a))         # gia tri tuyet doi
print(round(b))       # lam tron
print(round(b, 2))    # lam tron 2 chu so thap phan
print(pow(c, 2))      # c mu 2
print(divmod(c, d))   # tra ve (thuong, du) dang tuple


# Bài 3.3: vận dung
print("[Vận dung]")
import math

# Khai báo các hệ số a, b, c
a, b, c = 1, -3, 2

# Tính toán delta và 2 nghiệm phân biệt
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

# In kết quả ra màn hình
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")
