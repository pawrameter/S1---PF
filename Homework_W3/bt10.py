# Bài 10 - Rút tiền ATM

PIN = '1234'

balance = int(input('Nhập số dư tài khoản: '))
withdraw_amount = int(input('Nhập số tiền muốn rút: '))
pin = input('Nhập mã PIN: ')

if pin != PIN:
    print('Sai mã PIN')

else:
    if withdraw_amount <= 0:
        print('Số tiền không hợp lệ')

    elif withdraw_amount > balance:
        print('Số dư không đủ')

    elif withdraw_amount % 50000 != 0:
        print('Chỉ rút được bội số của 50000')

    else:
        balance = balance - withdraw_amount
        print('Rút tiền thành công')
        print(f'Số dư còn lại: {balance:,} VND')