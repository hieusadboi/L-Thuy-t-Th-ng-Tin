# câu 1
def cau1():
    name = input("nhap ten nguoi dung")
    print("Hello " + name + " Welcome to Python")

#cau1()

def cau2():
    while(True):
        n = int(input("nhap vao so n, 0<n<10."))
        if 0 < n < 10:
            break
        print("so ban nhap khong hop le.")
    result = n + int(f"{n}{n}") + int(f"{n}{n}{n}") + int(f"{n}{n}{n}{n}")
    print(f"{n} + {n}{n} + {n}{n}{n} + {n}{n}{n}{n} = {result}" )

#cau2()

def cau3():
    a = int(input("nhap vao so a"))
    while(True): 
        b = int(input("nhap vao so b != 0"))
        if b != 0:
            break
    
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    print(f"{a} / {b} = {a/b}")
    print(f"{a} ** {b} = {a**b}")

#cau3()

def cau4():
    while(True):
        r = float(input("nhap vao ban kinh hinh tron"))
        if r >= 0:
            break
    print(f"Chu vi = {2*3.14*r}")
    print(f"Dien tich = {3.14 *r ** 2}")

#cau4()

def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*giaithua(n-1)

def cau5():
    while(True):
        n = int(input("nhap n >= 0\n"))
        if n >= 0:
            break
    print(f"giai thua {n} =  {giaithua(n)}")

#cau5()
import math
def cau6():
    a = int(input("nhap a:\n"))
    b = int(input("nhap b:\n"))
    c = int(input("nhap c:\n"))
    delta = b**2 - 4*a*c
    if a == 0 and b != 0:
        print(f"x = {-c/b}")
        return    
    if a == 0 and b == 0 and c != 0:
        print("phuong trinh vo nghiem")
        return
    if a == 0 and b == 0 and c == 0:
        print("phuong trinh vo so nghiem")
        return
    
    if delta < 0: print("phuong trinh vo nghiem")
    elif delta == 0: print(f"phuong trinh co nghiem kep x1 = x2 = {-b/2*a}")       
    else: 
        x1 =  (-b - math.sqrt(delta))/(2*a)
        x2 =  (-b + math.sqrt(delta))/(2*a)
        print(f"phuong trinh co 2 nghiem\nx1 = {x1} \n x1 = {x2}")
#cau6()
def cau7():
    for i in range(5000, 7000):
        if i % 7 == 0 and i % 5 != 0: 
            print(f"{i} ")
#cau7()

def cau8():
    n = int(input("Nhap vao so thap phan"))
    print(f"So nhi phan cua {n} la so {bin(n)[2:]}")
#cau8()
def cau9():
    while(True):
        a = int(input("nhap vao so duong a"))
        b = int(input("nhap vao so duong b"))
        if a > 0 and b > 0:
            break
    ucln = math.gcd(a,b)
    bcnn = (a*b)/ucln
    print(f"UCLN {a} va {b} = {ucln}\n")
    print(f"BCNN {a} va {b} = {bcnn}\n")
#cau9()


def cau12():
    while True: 
        n = int(input("Nhập số nguyên n: ")) 
        if n >= 0: break 
        print("Số phải lớn hơn hoặc bằng 0, vui lòng nhập lại.") 
    tong = sum(int(digit) for digit in str(n)) 
    print(f"Tổng các chữ số của {n} là: {tong}") 

#cau12()

def cau13(): 
    for i in range(1000, 2001): 
        if all(int(digit) % 2 != 0 
               for digit in str(i)): 
            print(f"{i}", end = " ")
            
#cau13()

import math

# Hàm tính entropy từ xác suất
def calculate_entropy(probabilities):
    entropy = 0
    for prob in probabilities:
        if prob > 0:
            entropy -= prob * math.log2(prob)
    return entropy

# Hàm tính xác suất của biến y (số đầu hình khi tung đồng xu)
def calculate_probability_y():
    # Xác suất hai lá bài cùng tên và khác tên
    p_same_name = 3 / 7
    p_diff_name = 4 / 7

    # Xác suất cho số lần đầu hình khi hai lá bài cùng tên
    p_heads_given_same = [1/4, 1/2, 1/4]  # 0, 1, 2 đầu hình tương ứng
    # Xác suất cho số lần đầu hình khi hai lá bài khác tên
    p_heads_given_diff = [1/8, 3/8, 3/8, 1/8]  # 0, 1, 2, 3 đầu hình tương ứng

    # Khởi tạo mảng xác suất y với 4 phần tử (0, 1, 2, 3 đầu hình)
    p_y = [0] * 4

    # Tính xác suất cho từng trường hợp đầu hình
    # Trường hợp 0 đầu hình
    p_y[0] = (p_same_name * p_heads_given_same[0]) + (p_diff_name * p_heads_given_diff[0])
    
    # Trường hợp 1 đầu hình
    p_y[1] = (p_same_name * p_heads_given_same[1]) + (p_diff_name * p_heads_given_diff[1])
    
    # Trường hợp 2 đầu hình
    p_y[2] = (p_same_name * p_heads_given_same[2]) + (p_diff_name * (p_heads_given_diff[2] + p_heads_given_diff[2]))
    
    # Trường hợp 3 đầu hình
    p_y[3] = (p_diff_name * p_heads_given_diff[3])

    return p_y

# Xác suất hai lá bài cùng tên (K hoặc Át)
p_same_name = 3 / 7  # Xác suất rút được 2 lá cùng tên (K hoặc Át)
p_diff_name = 4 / 7  # Xác suất rút được 2 lá khác tên

# Tính H(y): Entropy của việc hai lá bài có cùng tên hay không
mang = calculate_probability_y()
H_y = calculate_entropy(mang)

# Xác suất và entropy của biến x (số đầu hình khi tung đồng xu)
# Trường hợp 1: Khi hai lá bài cùng tên -> tung đồng xu 2 lần
# Xác suất cho số lần đầu hình: 0 đầu hình (1/4), 1 đầu hình (1/2), 2 đầu hình (1/4)
p_heads_2 = [1/4, 1/2, 1/4]
H_x_given_same_name = calculate_entropy(p_heads_2)

# Trường hợp 2: Khi hai lá bài khác tên -> tung đồng xu 3 lần
# Xác suất cho số lần đầu hình: 0 đầu hình (1/8), 1 đầu hình (3/8), 2 đầu hình (3/8), 3 đầu hình (1/8)
p_heads_3 = [1/8, 3/8, 3/8, 1/8]
H_x_given_diff_name = calculate_entropy(p_heads_3)

# Tính H(y/x): Entropy có điều kiện
H_y_given_x = p_same_name * H_x_given_same_name + p_diff_name * H_x_given_diff_name

# Tính lượng tin I(y|x)
I_y_given_x = H_y - H_y_given_x

# Tính xác suất cho biến y (số đầu hình khi tung đồng xu)
probability_y = calculate_probability_y()

# In kết quả
print(f"Entropy H(y): {H_y:.4f}")
print(f"Entropy có điều kiện H(y|x): {H_y_given_x:.4f}")
print(f"Lượng tin I(y/x): {I_y_given_x:.4f}")
print(f"Xác suất cho biến y (số đầu hình): {probability_y}")
