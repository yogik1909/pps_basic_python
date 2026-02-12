expenses = []


def add_expense(expenses: list[float], value: float):
    expenses.append(value)

def delete_expence(expenses: float, index: int):
    expenses.pop(index)

def get_total(expenses: list[float]):
    return sum(expenses)
    
def get_average(expenses: list[float]):
    return sum(expenses) / len(expenses)

def print_report(expenses: list[float]):
    print(expenses)


while True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")
    choice = input("Выберите действие: ")
    match choice:
        # 1. Добавить расход
        case "1":
            value = float(input("Введите сумму расхода: "))
            add_expense(expenses, value)
            print("Расход добавлен")
        # 2. Показать все расходы
        case "2":
            print_report(expenses)
        case "3":
            # 3. Показать сумму и средний расход
            print(f"Сумма расходов: {get_total(expenses)}")
            print(f"Средний расход: {get_average(expenses)}")
        case "4":
            # 4. Удалить расход по номеру
            index = int(input("Введите номер расхода: "))
            delete_expence(expenses, index)
            print("Расход на сумму {value} удален")
        case "5":
            exit()
        case _:
            print("\033[H\033[J", end="")
            continue

