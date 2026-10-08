# Bài 2 - Cây ATM rút tiền

# Giả định đang có 100tr trong tài khoản, hạn mức rút tiền là 20tr, và khách nhập số tiền cần rút luôn là bội số của 50.000
balance = 100000000

withdraw_amount = int(input('Nhập số tiền cần rút: '))

if withdraw_amount > balance:
    print('Số dư tài khoản không đủ')

elif withdraw_amount <= 0 or withdraw_amount > 20000000:
    print('Số tiền không thuộc hạn mức giao dịch cho phép')
    exit()

else:
    print(f'Nhập số tiền cần rút: {withdraw_amount:,}')

    num_500k = withdraw_amount // 500000
    print(f'500.000 đ: {num_500k} tờ')

    num_200k = withdraw_amount % 500000 // 200000
    print(f'200.000 đ: {num_200k} tờ')

    num_100k = withdraw_amount % 500000 % 200000 // 100000
    print(f'100.000 đ: {num_100k} tờ')

    num_50k = withdraw_amount % 500000 % 200000 % 100000 // 50000
    print(f' 50.000 đ: {num_50k} tờ')

    total_num = num_500k + num_200k + num_100k + num_50k
    print(f'Tổng số tờ: {total_num}')