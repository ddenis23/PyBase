import random

lower = "abcdefghjklmnoprsqtuvwxyz"
upper = "ABCDEFGHJKLMNOPRSQTUWRXYZ"
number = "0123456789"
symbol = "!@#$%^&*()"

all_strings = lower + upper + number + symbol
# print(all_strings)

lenght = 16
password = "".join(random.sample(all_strings, lenght))
print(password)