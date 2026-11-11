# Bài 8 - Kiểm tra tam giác

a = int(input('Nhập cạnh a: '))
b = int(input('Nhập cạnh b: '))
c = int(input('Nhập cạnh c: '))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print('Không phải tam giác')

elif a == b == c:
    print('Tam giác đều')

elif a == b or a == c or b == c:
    print('Tam giác cân')

elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
    print('Tam giác vuông')

else:
    print('Tam giác thường')

# Cần kiểm tra "tam giác đều" trước "tam giác cân" vì nếu bộ dữ liệu là tam giác đều thì bộ dữ liệu này sẽ thỏa mãn điều kiện của tam giác cân, chương trình sẽ dừng lại và print kết quả là "tam giác cân".
# Nếu đảo thứ tự thì bộ (4,4,4) cho kết quả là "tam giác cân".