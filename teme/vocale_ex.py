text = input("Introdu un text: ")

vocale = "aeiouAEIOU"
numar_vocale = 0

for litera in text:
    if litera in vocale:
        numar_vocale += 1

print(f"Numărul total de vocale este: {numar_vocale}")