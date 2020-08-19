# №100.txt - Ошибка PE

def get_bag(menu, cookbook, fridge):
    need_product = {}
    for dish in menu:
        num_need_dish = menu[dish]

        if dish in cookbook:
            for product in cookbook[dish]:
                if product in cookbook:
                    num_need_product = cookbook[dish][product]
                    for ingredient in cookbook[product]:
                        if ingredient in need_product:
                            need_product[ingredient] += cookbook[product][ingredient] * num_need_dish * num_need_product
                        else:
                            need_product[ingredient] = cookbook[product][ingredient] * num_need_dish * num_need_product
                else:
                    if product in need_product:
                        need_product[product] += cookbook[dish][product] * num_need_dish
                    else:
                        need_product[product] = cookbook[dish][product] * num_need_dish
        else:
            if dish in need_product:
                need_product[dish] += menu[dish]
            else:
                need_product[dish] = menu[dish]

    for ing in fridge:
        if ing in need_product:
            need_product[ing] -= fridge[ing]

    pre_result = sorted(list(need_product.items()), key=lambda x: x[0])

    result = []
    for i, j in pre_result:
        if j != 0:
            result.append([i, j])

    return result


number_banks = int(input().strip(" "))

for _ in range(number_banks):
    N, K, F = [int(el) for el in input().strip(" ").split()]

    menu = {}
    for _ in range(N):
        dish_name, dish_amount = input().strip(" ").split()
        menu[dish_name.strip(" ")] = int(dish_amount)

    cookbook = {}
    for _ in range(K):
        dish_name, R_i = input().strip(" ").split()
        ingredients = {}
        for _ in range(int(R_i)):
            ingredient_name, ingredient_amount = input().strip(" ").split()
            ingredients[ingredient_name.strip(" ")] = int(ingredient_amount)

        cookbook[dish_name.strip(" ")] = ingredients

    fridge = {}
    for _ in range(F):
        product_name, product_amount = input().strip(" ").split()
        fridge[product_name.strip()] = int(product_amount)

    res = get_bag(menu, cookbook, fridge)

    if res:
        for i in range(len(res) - 1):
            print(f"{res[i][0]} {res[i][1]}")
        print(f"{res[-1][0]} {res[-1][1]}", end='')
    else:
        print(end='')
