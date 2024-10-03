secret_number = 1886

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    user_number = int(input("Enter your guess: "))
    if user_number != secret_number:
        print("Ха-ха! Ви застрягли у моїй петлі!")
    else:
        print("Молодець, магле! Тепер ти вільний.")
        print("Секретне число було:", secret_number)
        break