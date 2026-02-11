class ConvertorTemperatura:
    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def ruleaza(self):
        print("Alege conversia:")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")

        optiune = input("Introdu optiunea (1 sau 2): ")

        if optiune == "1":
            temp = float(input("Introdu temperatura in Celsius: "))
            rezultat = self.celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {rezultat}°F")

        elif optiune == "2":
            temp = float(input("Introdu temperatura in Fahrenheit: "))
            rezultat = self.fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {rezultat}°C")

        else:
            print("Opțiune invalidă!")

convertor = ConvertorTemperatura()
convertor.ruleaza()
