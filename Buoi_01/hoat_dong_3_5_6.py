
# Hoat dong 3.2: Dat ten bien theo PEP 8

ten = "Lê Thị Mai Anh"
diem_toan = 9.5
diem_van = 9.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Ho ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)


# Hoat dong 4: Tu khoa Python

import keyword

print("Danh sach tu khoa Python:")
print(keyword.kwlist)
print("So luong tu khoa:", len(keyword.kwlist))


# Hoat dong 5.1: Toan tu so hoc

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


# Hoat dong 5.2: Toan tu so sanh va logic

diem = 6.5
tuoi = 20

dat_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60
phu_dinh_dieu_kien = not chua_du_18_hoac_tren_60

print("Dat loai Kha?", dat_kha)
print("Chua du 18 hoac tren 60?", chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien tren?", phu_dinh_dieu_kien)



# Hoat dong 5.3: Toan tu gan

x = 10

x += 5
print("Sau += 5:", x)

x -= 3
print("Sau -= 3:", x)

x *= 2
print("Sau *= 2:", x)

x /= 4
print("Sau /= 4:", x)

x //= 2
print("Sau //= 2:", x)

x **= 3
print("Sau **= 3:", x)


# Toan tu in
danh_sach = [1, 2, 3, "python"]
print("So 3 co trong danh sach?", 3 in danh_sach)


# Toan tu is
ds_1 = [1, 2, 3]
ds_2 = ds_1
ds_3 = [1, 2, 3]

print("ds_1 is ds_2:", ds_1 is ds_2)
print("ds_1 is ds_3:", ds_1 is ds_3)


# Hoat dong 5.4: Do uu tien toan tu

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)


# Hoat dong 6.1: Bien va Dynamic Typing

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))



# Hoat dong 6.2: Tinh diem trung binh va xep loai

ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))
