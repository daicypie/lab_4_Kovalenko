def calculate_pyramid_height(blocks):
    height = 0
    layer = 1

    while blocks >= layer:
        blocks -= layer
        height += 1
        layer += 1

    return height

blocks = int(input("Введіть кількість блоків: "))
height = calculate_pyramid_height(blocks)
print(f"Висота піраміди: {height}")

