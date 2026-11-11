# Bài 13 - Tính phí giao hàng

weight = float(input('Khối lượng kiện hàng (kg): '))
distance = float(input('Khoảng cách (km): '))
delivery_type = input('Loại giao hàng (nhanh/thuong): ')

if weight <= 0 or distance <= 0:
    print('Dữ liệu không hợp lệ')
    exit()

elif weight > 30:
    print('Không nhận kiện hàng quá nặng')
    exit()

elif weight <= 10:
    extra_cost = 0

else:
    extra_cost = 15000

if delivery_type == 'thuong':
    if distance > 10:
        total_cost = 20000 + (distance - 10) * 2000 + extra_cost
    else: 
        total_cost = 20000 + extra_cost

elif delivery_type == 'nhanh':
    if distance > 10:
        total_cost = 40000 + (distance - 10) * 4000 + extra_cost
    else:
        total_cost = 40000 + extra_cost

else:
    print('Loại giao hàng không hợp lệ')
    exit()

print(f'Tổng phí vận chuyển: {int(total_cost):,} VND')