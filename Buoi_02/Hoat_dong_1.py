# Hoạt động 1: Nhập/xuất dữ liệu & định dạng chuỗi

#Bài 1.1:input() và ép kiểu
print("[Bài 1.1: Input() và ép kiểu]")
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))


#Bài 1.2: print() và set/end
print("[Bài 1.2: print() và set/end]")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Dong 1", end=" | ")
print("Dong 2")

#Bài 1.3: So sánh 3 cách định dạng chuỗi
print("[Bài 1.3: So sanh 3 cách định dạng chuỗi]")
# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))