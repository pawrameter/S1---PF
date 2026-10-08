last_name = input('Nhập họ: ')
middle_name = input('Nhập tên đệm: ')
first_name = input('Nhập tên: ')
student_id = input('Nhập mã sinh viên: ')

print(f'Nhập họ: {last_name}')
print(f'Nhập tên đệm: {middle_name}')
print(f'Nhập tên: {first_name}')
print(f'Nhập mã sinh viên: {student_id}')

name = last_name + ' ' + middle_name + ' ' + first_name
print(f'Họ tên: {name}')

email = first_name + student_id + '@fpt.edu.vn'
print(f'Email: {email}')

banner_content = 'Welcome' + ' ' + last_name + ' ' + middle_name + ' ' + first_name + '!'
banner_length = len(banner_content)
banner_width = banner_length + 4
border = '*' * banner_width

print(border)
print(f'* {banner_content} *')
print(border)

print(f'Sinh viên Hà Nội: {'GCH' in student_id}')
print(f'Email hợp lệ: {'@' and 'edu' in email}')
