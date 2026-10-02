# HOẠT ĐỘNG 1: LIST CƠ BẢN

# Bài tập 1.1 - Khai báo & truy cập
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print("Phần tử đầu tiên:", diem_so[0])
print("Phần tử cuối cùng:", diem_so[-1])
print("Từ vị trí 1 đến trước 4:", diem_so[1:4])
print("Lấy cách 1 phần tử:", diem_so[::2])
print("Đảo ngược danh sách:", diem_so[::-1])


# Bài tập 1.2 - Các phương thức thường dùng
ten_sv = ["Mai Anh ", "Binh", "Chi"]

ten_sv.append("Dung")
ten_sv.insert(1, "Em")

print("\nDanh sách sau append và insert:")
print(ten_sv)

ten_sv.remove("Chi")

pop_ra = ten_sv.pop()

print("Danh sách sau remove và pop:", ten_sv)
print("- Đã xóa:", pop_ra)

ten_sv.sort()
print("Sau khi sắp xếp tăng dần:", ten_sv)

ten_sv.reverse()
print("Sau khi đảo ngược:", ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print("Sau khi extend:", ten_sv)


# HOẠT ĐỘNG 2: DUYỆT LIST BẰNG FOR

# Bài tập 2.1
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

tong = 0

print("\nCác điểm:")
for diem in diem_so:
    print(diem)
    tong = tong + diem

print("Tổng điểm:", tong)
print("Điểm trung bình:", round(tong / len(diem_so), 2))


# Bài tập 2.2 - List lồng nhau
ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMa trận theo từng hàng:")
for hang in ma_tran:
    print(hang)

print("\nTừng phần tử trong ma trận:")
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# Tính tổng tất cả phần tử
tong = 0

for hang in ma_tran:
    for phan_tu in hang:
        tong = tong + phan_tu

print("Tổng tất cả phần tử trong ma trận:", tong)



# HOẠT ĐỘNG 3: LIST COMPREHENSION

# Bài tập 3.1 - Lọc số chẵn/lẻ
day_so = list(range(1, 21))

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("\nSố chẵn:", so_chan)
print("Số lẻ:", so_le)


# Bài tập 3.2 - Biến đổi phần tử
diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Điểm sau khi cộng 0.5:", diem_cong)