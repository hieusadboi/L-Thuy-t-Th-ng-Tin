# Câu 1
#even_numbers = []

# Duyệt qua các số từ 100 đến 300
# for number in range(100, 301):
#     # Chuyển số thành chuỗi để kiểm tra từng chữ số
#     digits = str(number)
    
#     # Kiểm tra nếu tất cả các chữ số đều là số chẵn
#     if all(int(digit) % 2 == 0 for digit in digits):
#         even_numbers.append(digits)

# In các số ra, cách nhau bởi dấu phẩy
#print(",".join(even_numbers))

# Câu 2

# Yêu cầu người dùng nhập vào các số
#user_input = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")

# Chuyển dãy số thành danh sách các số nguyên
#numbers = [int(n) for n in user_input.split(",")]

# Lọc ra các số lẻ
#odd_numbers = [str(n) for n in numbers if n % 2 != 0]

# In các số lẻ ra, cách nhau bởi dấu phẩy
#print(",".join(odd_numbers))

# Cau 3: 
# Tạo từ điển với key là các số từ 1 đến 20, value là bình phương của chúng
# square_dict = {i: i ** 2 for i in range(1, 21)}

# for key, value in square_dict.items():
#     print(f"{key}-{value}")


# Cau 4:
# Danh sách ban đầu
# lst = [12, 24, 35, 70, 88, 120, 155]

# # Xóa phần tử ở vị trí 0, 4, 5
# del lst[5]
# del lst[4]
# del lst[0]

# In danh sách sau khi xóa
#print(lst)


# Cau 5
# Danh sách 1

# list1 = [12, 3, 6, 78, 35, 55, 120]

# # Danh sách 2
# list2 = [12, 24, 35, 78, 88, 120, 155]

# # Tìm các phần tử chung (giao của 2 danh sách)
# intersection = list(set(list1) & set(list2))

# In danh sách giao
# print(intersection)


# Cau 6:
# Tạo danh sách chứa bình phương của các số từ 1 đến 20
#squares = [i ** 2 for i in range(1, 21)]

# In danh sách trừ 5 giá trị đầu tiên
#print(squares[5:])

# Cau 7:
# Nhập tuple gồm 7 số từ người dùng
# while True:
#     try:
#         user_input = tuple(int(input(f"Nhập số thứ {i+1}: ")) for i in range(7))
#         break
#     except ValueError:
#         print("Vui lòng nhập vào các số.")

# Tạo tuple chỉ chứa các số chẵn
#even_numbers = tuple(n for n in user_input if n % 2 == 0)

# In tuple chứa các số chẵn
#print(even_numbers)


# Cau 8:

# # Nhập câu từ người dùng

# sentence = input("Nhập vào một câu: ")

# # Tạo từ điển để đếm số lượng ký tự
# char_count = {}

# # Duyệt qua từng ký tự trong câu
# for char in sentence:
#     # Tăng số lượng của ký tự đó trong từ điển
#     char_count[char] = char_count.get(char, 0) + 1

# # In số lượng của từng ký tự
# for char, count in char_count.items():
#     print(f"{char} : {count}")


# Cau 9:

# # Nhập chuỗi từ người dùng
# sentence = input("Nhập vào một câu: ")

# # In chuỗi theo thứ tự ngược lại
# print(sentence[::-1])


# Cau 10:

# Nhập chuỗi từ người dùng và đảm bảo chuỗi có ít nhất 2 ký tự
# while True:
#     user_input = input("Nhập vào một chuỗi: ")
    
#     # Kiểm tra chiều dài chuỗi phải lớn hơn hoặc bằng 2
#     if len(user_input) >= 2:
#         # Tạo chuỗi mới từ 2 ký tự đầu và 2 ký tự cuối
#         new_string = user_input[:2] + user_input[-2:]
#         # In chuỗi mới
#         print(f"Chuỗi mới: {new_string}")
#         break
#     else:
#         print("Chuỗi quá ngắn, vui lòng nhập lại.")


# Câu 11:

# Nhập 2 chuỗi từ người dùng
# string1 = input("Nhập chuỗi 1: ")
# string2 = input("Nhập chuỗi 2: ")

# # Hoán đổi 2 ký tự đầu của 2 chuỗi và tạo chuỗi mới
# new_string1 = string2[:2] + string1[2:]
# new_string2 = string1[:2] + string2[2:]

# # In chuỗi kết quả
# result = new_string1 + ", " + new_string2
# print(result)

# Câu 13:

# Nhập chuỗi từ người dùng
# user_input = input("Nhập vào một chuỗi: ")

# # Lấy ký tự đầu tiên
# first_char = user_input[0]

# # Thay thế tất cả các ký tự trùng lặp của ký tự đầu tiên bằng "@"
# result = first_char + user_input[1:].replace(first_char, "@")

# # In chuỗi kết quả
# print(result)


# Câu 14:

def getsuffix(a, b):
    # Tạo một tập rỗng để lưu các hậu tố
    suffix_set = set()

    # Duyệt qua từng chuỗi trong list a và b
    for str_a in a:
        for str_b in b:
            # Kiểm tra nếu str_a là tiền tố của str_b
            if str_b.startswith(str_a) and str_a:
                # Sử dụng rsplit để tách phần hậu tố từ str_b
                suffix = str_b.rsplit(str_a, 1)[-1]
                suffix_set.add(suffix)
            
            # Kiểm tra nếu str_b là tiền tố của str_a
            elif str_a.startswith(str_b) and str_b:
                # Sử dụng rsplit để tách phần hậu tố từ str_a
                suffix = str_a.rsplit(str_b, 1)[-1]
                suffix_set.add(suffix)

    # Trả về tập chứa các hậu tố tìm được
    return suffix_set

# Câu 15
def kiemtrabangma(a):
    # Khởi tạo 2 list S0 và S1
    S0 = a  # S0 là bảng mã ban đầu
    S1 = getsuffix(S0, S0)  # Lấy các hậu tố của S0 với chính nó
    if not S1:
        print("Đây là bảng mã tách được\n")
        return True
    else:
        previous_state=[]
        while S1:
            if S1 in previous_state:
                print("Đây là bảng mã không tách được")
                return False
            
            previous_state.append(S1)
            # Tạo biến S2 kiểu Set, lưu các hậu tố giữa S0 và S1
            S2 = getsuffix(S0, S1)
            # Kiểm tra nếu S2 giao với S0 có phần tử nào (Stemp)
            Stemp = S2.intersection(S0)
            # Nếu S2 rỗng, bảng mã tách được
            if not S2:
                print("Đây là bảng mã tách được")
                return True

            # Nếu Stemp (giao giữa S2 và S0) không rỗng, bảng mã không tách được
            elif Stemp:
                print("Đây là bảng mã không tách được")
                return False

            # Nếu S2 bằng S1 (S2 không thay đổi so với lần trước), bảng mã không tách được
            elif S2 == S1 or S2 == S0:
                print("Đây là bảng mã không tách được")
                return False

            # Cập nhật S1 cho vòng lặp tiếp theo
            S1 = S2


# Câu 16

a = {"a", "c", "ad", "abb", "bad", "deb", "bbcde"}
kiemtrabangma(a)

b = {"abc", "a", "ab", "b", "bcad"}
kiemtrabangma(b)

c = {"a", "ad", "bbcde", "c", "deb", "ebd"}
kiemtrabangma(c)

d = {"a", "ad", "bbcde", "c", "deb", "ebad"}
kiemtrabangma(d)


