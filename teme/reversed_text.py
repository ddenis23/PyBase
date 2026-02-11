def inverseaza_text(text):
    return text[::-1]


text = input("Introdu un text: ")
text_inversat = inverseaza_text(text)

print("Text inversat:", text_inversat.lower())