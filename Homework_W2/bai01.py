# Bài 1 - Hóa đơn quán cà phê

coffee_price = int(input('Nhập giá cà phê sữa: '))
num_coffee = int(input('Nhập số ly cà phê sữa: '))
peachtea_price = int(input('Nhập giá trà đào: '))
num_peachtea = int(input('Nhập số ly trà đào: '))

print(f'Nhập giá cà phê sữa: {coffee_price}')
print(f'Nhập số ly cà phê sữa: {num_coffee}')
print(f'Nhập giá trà đào: {peachtea_price}')
print(f'Nhập số ly trà đào: {num_peachtea}')

double_line = '=' * 30
print(double_line)

name = 'TUAN 2 COFFEE'
print(f'{name:^30}')

print(double_line)

total_cup_coffee = f'Ca phe sua x{num_coffee}'
total_cup_peachtea = f'Tra dao x{num_peachtea}'
cost_coffee = coffee_price * num_coffee
cost_peachtea = peachtea_price * num_peachtea

print(f'{total_cup_coffee:<18} {cost_coffee:>11.2f}')
print(f'{total_cup_peachtea:<18} {cost_peachtea:>11.2f}')

single_line = '-' * 30
print(single_line)

subtotal = cost_coffee + cost_peachtea
print(f'{'Tam tinh':<18} {subtotal:>11.2f}')

vat = subtotal * 0.08
print(f'{'VAT 8%':<18} {vat:>11.2f}')

total_cost = subtotal + vat
print(f'{'Tong cong':<18} {total_cost:>11.2f}')

print(double_line)