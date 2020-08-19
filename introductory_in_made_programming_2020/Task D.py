def get_result(stack):
    if len(stack) == 0:
        return 'CORRECT'
    elif len(stack) == 1:
        return 'ALMOST' + ' ' + stack[0]

    else:
        if (len(stack) - 1) % 2 == 0:
            check_one_incorrect = True
            for i in range(len(stack) // 2):
                _mult = (stack[i] == stack[-(i + 1)].replace('/', '') and '/' in stack[-(i + 1)])
                check_one_incorrect *= _mult

            if check_one_incorrect:
                return 'ALMOST ' + stack[len(stack) // 2]
            else:
                return 'INCORRECT'
        else:
            return 'INCORRECT'


number_banks = int(input().strip())

for _ in range(number_banks):
    number_tags = int(input().strip())
    tags = []
    for _ in range(number_tags):
        tags.append(input().strip().upper())

    stack = []

    for i in range(len(tags)):
        tag = tags[i]

        if len(stack) >= 1:
            if stack[-1] == tag.replace('/', '') and '/' in tag:
                stack.pop()
            else:
                stack.append(tag)
        else:
            stack.append(tag)

    print(get_result(stack))
