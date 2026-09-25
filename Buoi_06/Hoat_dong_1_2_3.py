# HOẠT ĐỘNG 1 - HÀM CƠ BẢN
print("[ HOẠT ĐỘNG 1 - HÀM CƠ BẢN ]")

# Bài 1.1
print("[ Bài 1.1 ]")
# Hàm tìm ước số chung lớn nhất
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Hàm tìm bội số chung nhỏ nhất
def bscnn(a, b):
    return a * b // uscln(a, b)


# Hàm kiểm tra số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Hàm kiểm tra số hoàn thiện
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0

    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# GỌI HÀM VÀ KIỂM TRA KẾT QUẢ


print("USCLN:")
print(uscln(24, 36))
print(uscln(15, 25))
print(uscln(18, 30))

print("\nBSCNN:")
print(bscnn(4, 6))
print(bscnn(8, 12))
print(bscnn(5, 10))

print("\nKIỂM TRA SỐ NGUYÊN TỐ:")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(17))
print(kiem_tra_nguyen_to(20))

print("\nKIỂM TRA SỐ HOÀN THIỆN:")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(10))



# BÀI 1.2
print("[ Bài 1.2 ]")

# Hàm không trả về giá trị
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return


# Hàm trả về nhiều giá trị
def chia_lay_thuong_du(a, b):
    return a // b, a % b


# Gọi hàm in lời chào
in_loi_chao("An")


# Gọi hàm chia lấy thương và dư
thuong, du = chia_lay_thuong_du(17, 5)

print(f"Thuong: {thuong}, du: {du}")





# HOẠT ĐỘNG 2 - THAM SỐ MẶC ĐỊNH
#          VÀ THAM SỐ TỪ KHÓA
print("[ HOẠT ĐỘNG 2 - Tham số mặc định và tham số từ khóa ]")

def gioi_thieu(ten, tuoi=20, lop="DH14C1"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")


# 1. Sử dụng toàn bộ giá trị mặc định
gioi_thieu("Mai Anh ")


# 2. Ghi đè giá trị tuổi
gioi_thieu("Tan ", 25)


# 3. Sử dụng tham số từ khóa
gioi_thieu("Chi", lop="CNTT01")


# 4. Sử dụng các tham số từ khóa
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)



# HOẠT ĐỘNG 3 - THAM SỐ LINH HOẠT
print("[ HOẠT ĐỘNG 3 - THAM SỐ LINH HOẠT ]")
# Bài 3.1 - *args
print("[ Bài 3.1 - *args ]")
def tinh_tong(*args):
    tong = 0

    for so in args:
        tong += so

    return tong


# Gọi hàm với 3 số
print(tinh_tong(1, 2, 3))

# Gọi hàm với 5 số
print(tinh_tong(5, 10, 15, 20, 25))

# Không truyền số nào
print(tinh_tong())

# Bài 3.2 - **kwargs
print("[ Bài 3.2 - **kwargs ]")
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")

    for khoa, gia_tri in kwargs.items():
        print(f" {khoa}: {gia_tri}")


# Trường hợp 1
in_thong_tin(
    "Le Thi Mai Anh",
    20,
    lop="CNTT01",
    que_quan="Nam Dinh "
)

# Trường hợp 2
in_thong_tin(
    "Bui Nhat Tan ",
    25,
    email="lma146626@gmail.com"
)