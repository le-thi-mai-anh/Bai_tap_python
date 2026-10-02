# MINI PROJECT 2
# QUẢN LÝ KHO HÀNG


# Mỗi sản phẩm có dạng:
# (Tên sản phẩm, Giá, Số lượng)

kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]


# 1. THÊM SẢN PHẨM MỚI


kho_hang.append(
    ("Tai nghe", 300000, 15)
)



# 2. XÓA SẢN PHẨM

kho_hang.remove(
    ("Chuot", 150000, 20)
)



# 3. HIỂN THỊ DANH SÁCH KHO HÀNG


print("DANH SÁCH KHO HÀNG:")

for ten, gia, so_luong in kho_hang:
    print(
        f"{ten:<12} - Giá: {gia:>10,} - SL: {so_luong}"
    )



# 4. TÍNH TỔNG GIÁ TRỊ KHO HÀNG


tong_gia_tri = 0

for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(
    f"\nTổng giá trị kho hàng: {tong_gia_tri:,} VND"
)