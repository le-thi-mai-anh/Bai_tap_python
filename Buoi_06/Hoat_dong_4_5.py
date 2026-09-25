# HOẠT ĐỘNG 4 - PHẠM VI BIẾN
# LOCAL, GLOBAL VÀ TỪ KHÓA GLOBAL
print("[ HOẠT ĐỘNG 4 - PHẠM VÍ BIẾN , LOCAL , GLOBAL VÀ  TỪ KHÓA GLOBAL ]")


# Biến global
so_luot_truy_cap = 0


# Hàm tăng số lượt truy cập
def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


# Hàm minh họa biến local
def vi_du_bien_local():
    so_luot_truy_cap = 100
    print("Ben trong ham, bien local =", so_luot_truy_cap)


# Gọi hàm tăng lượt truy cập 2 lần
tang_luot_truy_cap()
tang_luot_truy_cap()


# In biến global
print("So luot truy cap (global):", so_luot_truy_cap)


# Gọi hàm có biến local
vi_du_bien_local()


# Kiểm tra lại biến global
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)


# HOẠT ĐỘNG 5
# LAMBDA + MAP + FILTER + SORTED
print("[ HOẠT ĐỘNG 5 - LAMBDA + MAP + FILTER + SORTED ]")


# BÀI 5.1 - map() với lambda
print("[ Bài 5.1 - map() với lambda ]")

danh_sach_so = [1, 2, 3, 4, 5]

binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))

print(binh_phuong)


# BÀI 5.2 - filter() với lambda
print("[ Bài 5.2 - filter() với lambda ]")
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))

print(so_chan)


# BÀI 5.3 - sorted() với lambda
print("[ Bài 5.3 - sỏted() với lambda ]")

danh_sach_sv = [
    {"ten": " Minh Khôi ", "diem": 8.5},
    {"ten": "Bảo Linh ", "diem": 5.0},
    {"ten": "Mai Anh", "diem": 9.8},
    {"ten": "Hải Anh" , "diem": 4.8},
    {"ten": "Ánh Phượng " , "diem": 8.6}
]


# Sắp xếp điểm tăng dần
sap_xep_theo_diem = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"]
)


# Sắp xếp điểm giảm dần
sap_xep_giam_dan = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"],
    reverse=True
)


# In kết quả tăng dần
for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])


print("--- Giam dan ---")


# In kết quả giảm dần
for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])