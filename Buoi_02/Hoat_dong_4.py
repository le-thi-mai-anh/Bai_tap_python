# Hoạt động 4: String -indexing ,...

# Bài 4.1: indexing & slicing
print("[ bài 4.1: indexing & slicing]")
cau = "Lap trinh Python rat thu vi"

print(cau[0])         # ky tu dau tien
print(cau[-1])        # ky tu cuoi cung
print(cau[4:10])      # cat tu vi tri 4 den truoc vi tri 10
print(cau[:8])        # tu dau den vi tri 8
print(cau[11:1])      # tu vi tri 11 den het
print(cau[::-1])      # dao nguoc chuoi

# Yêu cầu: in chuỗi đảo ngược và kiểm tra palindrome bằng biểu thức so sánh
chuoi_dao_nguoc = cau[::-1]
print("Chuoi dao nguoc:", chuoi_dao_nguoc)
print("Co phai Palindrome khong?:", cau == chuoi_dao_nguoc)

# Bài 4.2 : tính bất biến
print("[ bài 4.2: tính bất biến ]")
ten = "Nam"
# Thu gan lai mot ky tu: ten[0] = "T" -> quan sat loi TypeError
ten_moi = "T" + ten[1:]
print(ten_moi)

# Bài 4.3: Các phương thức xử lý chuỗi thường dùng
print("[ các phương thức xử lý chuỗi thương dùng ]")
cau = "  Toi dang HOC Python rat vui  "

print(cau.strip())
print(cau.strip().upper())
print(cau.strip().lower())
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split())
print(len(cau.strip().split()))
print(cau.count("o"))
print(cau.find("Python"))
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))


# Bài 4.4 : vận dụng
print (" Vận dụng ")
ho_ten_tho = "   nguyen   van   an  "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach)  # Nguyen Van An