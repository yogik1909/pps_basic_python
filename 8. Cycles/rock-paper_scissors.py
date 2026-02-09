# Реазизация игры камень, ножницы, бумага
# пользователь вводит число раудов
# Компьютер выбирает случайное число из списка
# У кого больше побед тот и победил
import random

a = ["ROC", "PAPER", "SCISSORS"]
# Компьютер выбирает случайное число из списка
computer_choice = random.choice(a)
# Пользователь вводит число раудов
num_round = int(input("Enter the number of rounds: "))
sum_res_use = 0
sum_res_comp = 0
for i in range(num_round):
    user_choice = input("Enter your choice: ")
    computer_choice = random.choice(a)
    
    match user_choice:
        case "ROC":
            if computer_choice == "SCISSORS":
                sum_res_use += 1
            else:
                sum_res_comp += 1
        case "PAPER":
            if computer_choice == "ROC":
                sum_res_use += 1
            else:
                sum_res_comp += 1
        case "SCISSORS":
            if computer_choice == "PAPER":
                sum_res_use += 1
            else:
                sum_res_comp += 1
        case _:
            print("Invalid choice")

print(f"You win {sum_res_use} times")
print(f"Computer win {sum_res_comp} times")
if sum_res_use > sum_res_comp:
    print("You win")
else:
    print("Computer win")