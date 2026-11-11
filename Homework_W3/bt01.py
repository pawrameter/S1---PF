# Bài 1 - Điều kiện bay drone

MAX_WIND_SPEED = 30

wind_speed = float(input('Nhập tốc độ gió (km/h): '))
raining_input = input('Trời có mưa không (y/n): ').lower()
is_raining = raining_input == 'y'

if wind_speed <= 0 or raining_input not in ['y', 'n']:
    print('Dữ liệu không hợp lệ')

else:
    if wind_speed <= MAX_WIND_SPEED and not is_raining:
        print('Có thể bay')
    else:
        print('Không thể bay')