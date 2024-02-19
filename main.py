kevin_age = 16

# +, -, /, *

my_result1 = kevin_age * 2
my_result2 = kevin_age / 2
my_result3 = kevin_age + 2
my_result4 = kevin_age - 2

print(kevin_age)
print("Alter*2", my_result1)
print("Alter/2", my_result2)
print("Alter+2", my_result3)
print("Alter-2", my_result4) 

if kevin_age > 18:
    print("Erwachsen")
elif kevin_age == 18:
    print("new adult!")
else:
    print("Minderjährig") 

for i in range(2):
    my_result1 = my_result1 * 2

print(my_result1)

bank_account_balances1 = [5322.0, 577.35, -100.0]
bank_account_balances2 = [322.0, 8577.35, -80.0]

def print_bank_account_info(bank_account_info):
    for balance in bank_account_info:
        print(balance)        

print_bank_account_info(bank_account_balances1)
print_bank_account_info(bank_account_balances2)
