# Bài 3 - Thời lượng khóa học online

total_second = int(input('Nhập tổng số giây: '))

if total_second <= 0:
    print(f'Invalid number')
    exit()
    
else:
    print(f'Nhập tổng số giây: {total_second}')
    
    day = total_second // 86400
    hour = total_second % 86400 // 3600
    minute = total_second % 86400 % 3600 // 60
    second = total_second % 86400 % 3600 % 60
    print(f'{total_second} giây = {day} ngày {hour} giờ {minute} phút {second} giây')

    hour_clock =  total_second // 3600
    minute_clock =  total_second % 3600 // 60
    second_clock = total_second % 3600 % 60
    print(f'Dạng đồng hồ: {hour_clock:02}:{minute_clock:02}:{second_clock:02}')
