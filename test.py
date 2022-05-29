
price = 1000000
buyer_credit = 'good' 
if buyer_credit == 'good':
    print ('Downpayment is 10%')
    Downpayment = 0.1 * int(price)
    print(Downpayment)
elif buyer_credit == 'no' :
    print('Downpayment is 20%')
    Downpayment = 0.2 * int(price)
    print(Downpayment)
else:
    print('cannot afford the house')


numbers = [30,22,11,23,54,5,76,10,23,91,27]
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number=number
        print(f'largest = {largest_number}')
    else:
        print(f'{number} is less than {largest_number}')


digits = []
for number in 30,22,40,23,54,11,23,54,5,76,10,23,91,27:
    if number not in digits:
        digits.append(number)
print(digits)
    

