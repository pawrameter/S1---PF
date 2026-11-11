# Bài 11 - Hành lý ký gửi khi đặt vé máy bay

ticket_class = input('Hạng vé (economy/business): ').lower()
baggage_weight = float(input('Số kg hành lý ký gửi: '))
membership = input('Có thẻ thành viên (y/n): ').lower()

if baggage_weight < 0 or membership not in ['y', 'n']:
    print('Dữ liệu không hợp lệ')

else: 
    if ticket_class == 'economy':
        if baggage_weight <= 20:
            baggage_fee = 0
        else:
            if membership == 'n':
                baggage_fee = int((baggage_weight - 20) * 50000)
            else:
                baggage_fee = int((baggage_weight - 20) * 50000 / 2)
        
        print(f'Phụ phí hành lý: {(baggage_fee):,} VND')

    elif ticket_class == 'business':
        if baggage_weight <= 40:
            baggage_fee = 0
        else:
            baggage_fee = int((baggage_weight - 40) * 50000)

        print(f'Phụ phi hành lý: {baggage_fee:,} VND')

    else:
        print('Hạng vé không hợp lệ')