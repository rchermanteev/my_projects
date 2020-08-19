
def delete_gen(gen_code):
    flag = False
    for sym in num_sym:
        if gen_code.find(f"{sym}{sym.upper()}") != -1:
            flag = True
            gen_code = gen_code.replace(f"{sym}{sym.upper()}", "")
        if gen_code.find(f"{sym.upper()}{sym}") != -1:
            flag = True
            gen_code = gen_code.replace(f"{sym.upper()}{sym}", "")

    if flag:
        return delete_gen(gen_code)

    return len(gen_code)


gen_code = input()
num_sym = set(gen_code.lower())
list_num = []

for sym in num_sym:
    code = gen_code
    code = code.replace(sym, "").replace(sym.upper(), "")
    list_num.append(delete_gen(code))

print(min(list_num))
