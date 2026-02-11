taskuri = []

def cere_nume():
    nume = input("Cum te numesti? ")
    return nume

def afiseaza_salut(nume):
    print(f"Salut, {nume}! Bine ai venit in asistentul tau zilnic.")

def meniu_task():
    meniu = [
        "1 - Adauga Task",
        "2 - Afiseaza toate Taskurile",
        "3 - Marcheaza un task ca facut ",
        "0 - Iesire"
    ]
    return meniu

def afiseaza_meniu(meniu):
    for optiune in meniu:
        print(optiune)

def adauga_task(taskuri):
    alegere_task = input("Ce task adaugam? ")
    taskuri.append(alegere_task)

def afiseaza_taskuri(taskuri):
    if len(taskuri) == 0:
        print("Nu ai niciun task in lista.")
    else:
        print("Task-urile tale sunt:")
        for i in range(len(taskuri)):
            print(f"{i+1}. {taskuri[i]}")

def sterge_task(taskuri):
    if len(taskuri) == 0:
        print("Nu ai niciun task in lista.")

def finalizeaza_task(taskuri):
    if len(taskuri) == 0:
        print("Nu ai niciun task de finalizat.")
        return

    print("Task-urile tale sunt:")
    for i in range(len(taskuri)):
        print(f"{i+1}. {taskuri[i]}")

    raspuns = input("Scrie numarul task-ului pe care vrei sa-l stergi: ")

    try:
        numar = int(raspuns)
    except ValueError:
        print("Trebuie sa scrii un numar, nu text.")
        return

    if 1 <= numar <= len(taskuri):
        index = numar - 1
        task_sters = taskuri.pop(index)
        print(f"Task-ul '{task_sters}' a fost sters cu succes.")
    else:
        print("Numar invalid! Nu exista niciun task cu acest numar.")

def main():
    nume = cere_nume()
    afiseaza_salut(nume)
    meniu = meniu_task()
    ruleaza = True
    while ruleaza:
        print()
        afiseaza_meniu(meniu)
        alegere = input("Ce vrei sa fac? ")
        if alegere == "1":
            adauga_task(taskuri)
            print("Taskul a fost adaugat cu succes in lista!")
        elif alegere == "2":
            afiseaza_taskuri(taskuri)
        elif alegere == "3":
            finalizeaza_task(taskuri)
        elif alegere == "0":
            ruleaza = False
            print("Ai iesit din asistent, la revedere!!")
        else:
            print("optiune invalida, ca tine")

main()
