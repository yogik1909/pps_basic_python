import random
import string


def generate_password(length: int, use_symbol: bool = True) -> str:
    if length < 3:
        return ""

    # Собираем все символы в одну строку
    characters = string.ascii_letters + string.digits

    if use_symbol:
        # Добавляем специальные символы
        characters += string.punctuation + "!@#$%&*^_=+"

    password = []
    while len(password) < length:
        char = random.choice(characters)
        if len(password) < len(characters) \
                and char in password:
            continue
        password.append(char)

    return "".join(password)


print(len(string.ascii_letters + string.digits + string.punctuation + "!@#$%&*^_=+"))
print(generate_password(32))
print(generate_password(10, False))
