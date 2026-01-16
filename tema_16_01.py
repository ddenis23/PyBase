raw_logs = [
    " ERROR | Voltage too LOW | code=E12 ",
    " info | System started successfully ",
    " WARNING | High temperature detected | code=W07 ",
    " ERROR | Communication timeout | code=E99 ",
    " info | System shutdown complete "
]

error_code = []
warning_code = []
levels = []
clean_logs = []
for i in raw_logs:
    clean_logs.append(i.strip().lower())

for i in clean_logs:
    parts = i.split("|")
    # print(parts)
    level = parts[0].strip()
    # print(levels)

    # Identificăm tipul
    if "error" in level and level.startswith("error"):
        levels.append("error")
    elif "warning" in level and level.startswith("warning"):
        levels.append("warning")
    elif "info" in level and level.startswith("info"):
        levels.append("info")

    # Extragem codurile
    for part in parts:
        part = part.strip()
        if "code=" in part:
            code = part.split("=")[1].upper()
            if level.startswith("error"):
                error_code.append(code)
            elif level.startswith("warning"):
                warning_code.append(code)

# Numărăm tipurile count()
error = levels.count("error")
warning = levels.count("warning")
info = levels.count("info")

report = (
    "LOG SUMMARY\n"
    "----------\n"
    f"Errors   : {error}\n"
    f"Warnings : {warning}\n"
    f"Info     : {info}\n\n"
    f"Error Codes: {', '.join(error_code)}\n"
    f"Warning Codes: {', '.join(warning_code)}"
)


print(report)