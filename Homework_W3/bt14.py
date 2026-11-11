# Bài 14 - Thuê xe tự lái

renter_age = int(input('Tuổi người thuê: '))
driving_exp = int(input('Số năm kinh nghiệm lái xe: '))
car_type = input('Loại xe (4 cho/7 cho): ')
rental_days = int(input('Số ngày thuê: '))

if renter_age < 21 or renter_age > 90:
    print('Không đủ tuổi thuê xe')
    exit()

if driving_exp < 1:
    print('Cần tối thiểu 1 năm kinh nghiệm')
    exit()

if car_type != '4 cho' and car_type != '7 cho':
    print('Loại xe không hợp lệ')
    exit()

if car_type == '7 cho' and driving_exp < 3:
    print('Xe 7 chỗ yêu cầu từ 3 năm kinh nghiệm')
    exit()

if car_type == '4 cho':
    base_rate = 800000
else:
    base_rate = 1200000

if rental_days < 7:
    discount_rate = 1
else:
    discount_rate = 0.9

total_cost = base_rate * rental_days * discount_rate

print(f'Tổng tiền thuê xe: {int(total_cost):,} VND')