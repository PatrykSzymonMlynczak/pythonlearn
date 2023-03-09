def run_app():
    user_choice = -1
    readFile = open("task.txt", "r")
    tasks = []

    for line in readFile:
        tasks.append(line)
    readFile.close()
    while user_choice != 5:
        if 1 > user_choice > 5:
            continue
        if user_choice == 1:
            task_index = 0
            for task in tasks:
                print(task + " :" + str(task_index))
                task_index += 1
        if user_choice == 2:
            task = input("wpisz zadanie: ")
            tasks.append(task)
        if user_choice == 3:
            task = input("podaj zadanie do usunięcia: ")
            if not task.isnumeric():
                index = tasks.index(task)
                tasks.pop(index)
            else:
                tasks.pop(int(task))
        if user_choice == 4:
            file = open("task.txt", "w+")
            file_length = len(tasks)
            index = 0
            for task in tasks:
                index += 1
                if index > file_length:
                    file.write(task + "\n")
                else:
                    file.write(task)

            file.close()
        try:
            user_choice = int(input("wybierz liczbę: "))
        except ValueError:
            print("To nie była liczba")
            continue


def print_menu():
    print("1. Pokaz zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zapisz do pliku")
    print("5. Wyjdź")


print_menu()
run_app()
