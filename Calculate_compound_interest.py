# estimated yearly interest

print('How many years will you be saving?')
years = int(input('Enter years: '))

print('How much money is currently in your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan in invest monthly?')
monthly_invest = float(input('Enter amount: '))

print('What do you estiate will be the yesrly interest of this investment?')
interest = float(input('Enter interest in decimal numbers(10% = 0.1): '))

print(' ')

monthly_invest12 = monthly_invest * 12
final_amount = 0

for i in range(0,years):
    if final_amount == 0:
        final_amount = principal

    final_amount = int((final_amount + monthly_invest12) * (1 + interest))

print('This is how much money you would have in your account after {} years: '.format(years) + str(final_amount))