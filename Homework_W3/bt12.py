# Bài 12 - Tuyển sinh đại học

total_score = float(input('Nhập tổng điểm 3 môn (0-30): '))
priority_zone = input('Khu vực ưu tiên (KV1/KV2/KV3): ')
priority_score = 0

if total_score < 0 or total_score > 30:
    print('Điểm không hợp lệ')

else: 
    if priority_zone == 'KV1':
        priority_score = 1.5
    elif priority_zone == 'KV2':
        priority_score = 1.0
    elif priority_zone == 'KV3':
        priority_score = 0
    else:
        print('Khu vực không hợp lệ')
        exit()

    admission_score = total_score + priority_score
    print(f'Điểm xét tuyển: {admission_score}')

    if admission_score >= 28:
        print('Đỗ vào ngành Công nghệ thông tin')
        print('Đủ điều kiện xét học bổng đầu vào')

    elif admission_score >= 24:
        print('Đỗ vào ngành Công nghệ thông tin')

    elif admission_score >= 20:
        print('Đỗ vào ngành Quản trị kinh doanh')

    else:
        print('Không đỗ')