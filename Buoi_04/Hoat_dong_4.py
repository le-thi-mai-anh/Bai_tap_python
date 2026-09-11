#Hoạt động 4: Chuyển đổi kiểu dữ liệu tường minh & ngầm định
print("\n========== HOAT DONG 4  ==========")
#Bài tập 4.1 - Ép kiểu tường minh:
print("[Bài tập 4.1 - Ép kiểu tường minh] ")
chuoi_so = "25"

# Chuyen chuoi "25" thanh so nguyen
so = int(chuoi_so)
print(so, type(so))

# Chuyen chuoi "3.14" thanh so thuc
so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

# Chuyen Tuple thanh List
danh_sach = list((1, 2, 3))

# Chuyen List thanh Tuple
bo_ba = tuple([4, 5, 6])

# Chuyen List thanh Set
# Set tu dong loai bo cac phan tu trung lap
tap_hop = set([1, 2, 2, 3, 3, 3])

# Chuyen danh sach cac Tuple thanh Dictionary
tu_dien = dict([("a", 1), ("b", 2)])

print(danh_sach, bo_ba, tap_hop, tu_dien)

#Bài tập 4.2 - Trường hợp gây lỗi khi ép kiểu
print("[Bài tập 4.2 - Trường hợp gây lỗi khi ép kiểu]")
 Truong hop 1: ep "abc" thanh int
print('Thu int("abc"):')
print(so1)


# Truong hop 2: ep "3.14" thanh int
print('Thu int("3.14"):')
so2 = int("3.14")
print(so2)


# Truong hop 3: ep "3.14" thanh float roi thanh int
print('Thu int(float("3.14")):')
so3 = int(float("3.14"))
print(so3)

#Bài tập 4.3: Chuyển đổi ngầm
print("[Bài tập 4.3: Chuyển đổi ngầm]")
# int + float
# Python tu dong chuyen ket qua thanh float
ket_qua = 5 + 2.5
print(ket_qua, type(ket_qua))

# Chuyen so thanh chuoi bang str()
ket_qua_2 = "Diem: " + str(8.5)
print(ket_qua_2)



