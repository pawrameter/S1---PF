# Bài 4 - Phí gửi xe chung cư

parking_hours= float(input('Nhập số giờ gửi xe: '))

if parking_hours <= 0:
    print('Dữ liệu không hợp lệ')
    exit()

elif parking_hours > 5:
    total_fee = 20000

elif parking_hours >= 2:
    total_fee = 10000

else:
    total_fee = 5000

print(f'Gửi {parking_hours} giở - Phí gửi xe: {total_fee:,} VND')