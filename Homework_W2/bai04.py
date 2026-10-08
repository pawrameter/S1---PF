# Bài 4 - Chia tiền đi xe công nghệ

base_fare = 12000
price_per_km = 4500
waiting_fee = 800

km = float(input('Nhập số km: '))
waiting_time = int(input('Nhập số phút chờ: '))
num_pp = int(input('Nhập số người trong nhóm: '))

if km <= 0 or waiting_time < 0 or num_pp <= 0:
    print('Invalid Distance / Waiting time / Number of Customers')
    exit()

else:
    print(f'Nhập số km: {km}')
    print(f'Nhập số phút chờ: {waiting_time}')
    print(f'Nhập số người: {num_pp}')

    total_cost = base_fare + price_per_km * km + waiting_fee * waiting_time
    print(f'Tổng tiền chuyến đi: {int(total_cost):,} đ')

    each_pays = (total_cost / num_pp // 1000) * 1000
    print(f'Mỗi người trả: {int(each_pays):,} đ')

    host_pays = total_cost / num_pp + (total_cost / num_pp - each_pays) * (num_pp - 1)
    print(f'Người đặt xe trả: {int(host_pays):,} đ')