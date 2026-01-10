produs = 1
# for i in range(5):
#     produs = produs * (i + 1)
# print(produs)
#
# import math
#
# produs = math.factorial(5)
# print(produs)

# doimea_nr = 121
# nr = doimea_nr * 2
# triplul_nr = nr * 3
# produs_numere_pare = 1
# for i in range(6):
#     if i % 2 == 0 and i != 0:
#         produs_numere_pare = produs_numere_pare *i
# nr_final = triplul_nr + produs_numere_pare
# print(nr_final)

#  //
# boxes = 53
# boxes_per_pallet = 10
# full_pallets = boxes//boxes_per_pallet
# print(full_pallets)

# ** - puterea unui numar
# modes = 3
# devices = 4
#
# combinations = modes**devices
# print(combinations)

# door_close = True
# emergency_stop_pressed = False
#
# start_machine = door_close and not emergency_stop_pressed
# print(start_machine)

# voltage_ok = True
# communication_ok = True
# test_failed = not voltage_ok or not communication_ok

# value = 42
#
# print(hex(value))

# &, |, ~
# 01100101
# READ = 0b001
# WRITE = 0b010
# EXEC = 0b100
#
# user_permissions = READ | WRITE
# print(bin(user_permissions))
#
# can_write = user_permissions & WRITE
# print(bin(can_write))

# s = "Hello World"
# print(s)

# print("""Primul rand
# Al doilea rand
# Al treilea rand """)

# test_name = "VoltageCheck"
# duration = 1.237
# print(test_name.lower())

# command = "StaRt"

# if command == "start":
#     print("Starting System")

# if command.lower() == "start":
#     print("Starting System")

# word = "pyhon"
# print(word[1])
# print(word[2])
# print(word[-
# text = "Programming"
# print(text[5:])

# message = "Hello Python"
# print(len(message))

# a = "hello"
# b = "world"
# # print(a+" "+b)
#
# raw = "   ERROR_CODE_12 "
#
# # strip
# clean_string = raw.strip()
# print(clean_string)

# replace()

# log = "Voltage=12,5V"
# log = log.replace(",",".")
# print(log)

#  ext.txt
#  file.abt
#  text.exe
#  file.log

# filename = "report_2025.exe"
# if filename.endswith(".log"):
#     print("Log file detected!")
# if filename.startswith("report"):
#     print("Report file detected!")

# find

# message = "Can timeout detected"
# # index = message.find("exit")
# # print(index)
# timeput_flag = False
# # in vs find
# if "timeout" in message:
#     timeout_flag = True
#     print("timeout detected")
#

# split()
# data = "12.5,3.7,OK"
# print(data)
# values = data.split(",")
# print(values)

# my_string = ["Ana ", "are ", "mere ", "!"]
# final_string = "".join(my_string)
# print(final_string)

# parts = ["C:", "logs", "2026", "run_01.txt"]
# path = "/".join(parts)
# print(path)

# Password generator
# import random
# string = "Ana are mere!"
# string_random = random.sample(string,3)
# print(string_random)

# lower = "abcdefghjklmnoprsqtuvwxyz"
# upper = "ABCDEFGHJKLMNOPRSQTUWRXYZ"
# number = "0123456789"
# symbol = "!@#$%^&*()"
#
# all_strings = lower + upper + number + symbol
# # print(all_strings)
#
# lenght = 16
# password = "".join(random.sample(all_strings, lenght))
# print(password)

# Function input
# a = ""
# while a != "STOP":
#     a = input("Add a data: ")
#     print(a)
# print("The user stopped entering the data!")

# LISTE

# my_list = [70, 1, -7, 50, True, "Ana are mere", 4+7j]
# # print(my_list)
# # print(my_list[-1])
# # print(len(my_list))
# # sliced_list = my_list[:4]
# # print(sliced_list)
# print(my_list[-3])

db = []
get_data = ""
while get_data != "STOP":
    get_data = input("Add a data: ")
    if get_data != "STOP": db.append(get_data)
print(db)