# HOẠT ĐỘNG 6 - ĐỆ QUY
print("[ HOẠT ĐỌNGO 6 - ĐỆ QUY ]")


# BÀI 6.1 - GIAI THỪA BẰNG ĐỆ QUY
print("[ Bài 6.1 - giai thừa bằng đệ quy ]")

def giai_thua_de_quy(n):
    if n <= 1:  # điều kiện dừng
        return 1

    return n * giai_thua_de_quy(n - 1)


# Giai thừa bằng vòng lặp
def giai_thua_lap(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


# So sánh hai cách
print("Giai thua bang de quy:", giai_thua_de_quy(5))
print("Giai thua bang vong lap:", giai_thua_lap(5))


# BÀI 6.2 - FIBONACCI BẰNG ĐỆ QUY
print("[ Bài 6.2 - fibonacci bằng đệ quy ]")

def fibonacci_de_quy(n):
    if n <= 1:  # điều kiện dừng
        return n

    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


# In 10 số Fibonacci đầu tiên
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")

print()