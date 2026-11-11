# Bài 2 - Ứng dụng lịch: kiểm tra năm nhuận

year = int(input('Nhập năm: '))

if year <= 0:
    print('Năm không hợp lệ')

else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f'{year}: Năm nhuận - tháng 2 có 29 ngày')
    else:
        print(f'{year}: Không phải năm nhuận - tháng 2 có 28 ngày')