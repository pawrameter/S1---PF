# Bài 2 - Quán cà phê: in hóa đơn

VAT = 8

def calc_subtotal(price, quantity):
    subtotal= price * quantity
    return subtotal

def calc_total(subtotal, discount_percent=0, vat_percent=VAT):
    total = subtotal * (1 - discount_percent/100) * (1 + vat_percent/100)
    return total

def print_receipt(item_name, price, quantity, discount_percent=0):
    subtotal = calc_subtotal(price, quantity)
    total = calc_total(subtotal, discount_percent)
    
    print('=' * 7 + ' THE BEAN ' + '=' * 7)

    print(f'{item_name} x {quantity} @ {price:,.0f}')
    print(f'Tiền hàng: {subtotal:>10,.0f} đ')
    print(f'Giảm giá: {discount_percent:>10} %')
    print(f'Tổng cộng: {total:>10,.0f} đ (đã gồm VAT {VAT}%)')

def main():
    item_name = input('Tên món: ')
    price = int(input('Đơn giá: '))
    quantity = int(input('Số lượng: '))
    membership = input('Có thẻ thành viên (y/n): ')
    
    discount_percent = 10 if membership.lower() == 'y' else 0

    print_receipt(item_name, price, quantity, discount_percent)

main()