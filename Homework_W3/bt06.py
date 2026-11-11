# Bài 6 - Tính tiền điện bậc thang

kwh = int(input('Nhập số kWh tiêu thụ: '))
print(f'Số điện: {kwh} kWh')

if kwh < 0:
    print('Dữ liệu không hợp lệ')
    exit()

elif kwh <= 50:
    total_fee = kwh * 1700

elif 50 < kwh <= 100:
    total_fee = 50 * 1700 + (kwh - 50) * 2000

else:
    total_fee = 50 * 1700 + 50 * 2000 + (kwh - 100) * 2500

print(f'Tiền điện phải trả: {total_fee:,} VND')