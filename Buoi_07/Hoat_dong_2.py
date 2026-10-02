# Hoạt động 2: Giới thiệu try-except
print("[ Hoạt động 2: Giới thiệu try-except ]")

#Chưa có try-except: nhập "abc" sẽ làm chương trình dừng đột ngột
#tuoi = int(input("Nhap tuoi: "))
#print("Tuoi cua ban la:", tuoi)

#Sử dụng try-except
try:
    tuoi = int(input("Nhap tuoi: "))
    print("Tuoi cua ban la:", tuoi)
except ValueError:
    print("Ban da nhap sai dinh dang, vui long nhap mot so nguyen.")

