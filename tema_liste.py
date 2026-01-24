raw_logs = [
    " ERROR | Voltage too LOW | code=E12 ",
    " info | System started successfully ",
    " WARNING | High temperature detected | code=W07 ",
    " ERROR | Communication timeout | code=E99 ",
    " info | System shutdown complete "
]

for i in range(len(raw_logs)):
    # for i -> creaza o variabila i
    # len(raw_logs) ---> 5
    raw_logs[i] = raw_logs[i].strip().lower()
    raw_logs[i] = raw_logs[i].split("|")



    # print(raw_logs[i])

print("Starting Identification")

log_type_counts = []

for i in range(len(raw_logs)):
    if raw_logs[i][0].startswith("error"):
        log_type_counts.append(raw_logs[i][0].strip())
        print("This is an error log")
    if raw_logs[i][0].startswith("info"):
        log_type_counts.append(raw_logs[i][0].strip())
        print("This is an info log")
    if raw_logs[i][0].startswith("warning"):
        log_type_counts.append(raw_logs[i][0].strip())
        print("This is an warning log")

error_counts = log_type_counts.count("error")
warning_counts = log_type_counts.count("warning")
info_counts = log_type_counts.count("info")

report = f'''
LOG SUMMARY
----------
Errors   : 
Warnings  : {error_counts}
Warnings : {warning_counts}
Info     : {info_counts}

Error Codes: E12, E99, E99, E99, E99, E99, E99
Warning Codes: W07
'''
# print("OUTPUT")
# print("LOG SUMMARY")
# print("----------------")
# print("Errors       :")
# print(log_type_counts.count("error"))
# print("Warnings     :")
# print(log_type_counts.count("warning"))
# print("Info         :")
#
# print("")

print(report)

