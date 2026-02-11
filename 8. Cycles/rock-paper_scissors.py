# Реазизация игры камень, ножницы, бумага
# пользователь вводит число раудов
# Компьютер выбирает случайное число из списка
# У кого больше побед тот и победил
import random

CHOISES = ["ROCK", "PAPER", "SCISSORS"]
# Пользователь вводит число раудов
num_round = int(input("Enter the number of rounds: "))
sum_res_use = 0
sum_res_comp = 0
user_choice = ""
for i in range(num_round):
    while user_choice not in CHOISES:
        user_choice = input("Enter your choice: ")

    computer_choice = random.choice(CHOISES)

    match user_choice:
        case "ROCK" if computer_choice == "SCISSORS":
            sum_res_use += 1
        case "PAPER" if computer_choice == "ROCK":
            sum_res_use += 1
        case "SCISSORS" if computer_choice == "PAPER":
            sum_res_use += 1
        case _:
            sum_res_comp += 1
    user_choice = ""

print(f"You win {sum_res_use} times")
print(f"Computer win {sum_res_comp} times")
if sum_res_use > sum_res_comp:
    print("You win")
elif sum_res_use == sum_res_comp:
    print("Draw")
else:
    print("Computer win")
