# Bài 5 - Gửi tiết kiệm ngân hàng

tien_goc = int(input('Nhập tiền gốc: '))
lai_suat = float(input('Nhập lãi suất: '))
so_nam = int(input('Nhập số năm: '))

if tien_goc <= 0 or lai_suat <= 0 or lai_suat > 30 or so_nam <= 0 or so_nam > 20:
    print('Số tiền gốc/Lãi suất/Số năm không hợp lý')
    exit()

else:
    print(f'Nhập tiền gốc: {tien_goc:,}')
    print(f'Nhập lãi suất (%/năm): {lai_suat}')
    print(f'Nhập số năm: {so_nam}')

    tien_cuoi_ky = tien_goc * (1 + lai_suat / 100) ** so_nam
    print(f'Tiền cuối kỳ: {tien_cuoi_ky:.2f}')

    tien_lai = tien_cuoi_ky - tien_goc
    print(f'Tiền lãi: {tien_lai:.2f}')

    tang = tien_lai / tien_goc * 100
    print(f'Tăng: {tang:.2f}%')