# №80.txt - Ошибка PE

def get_result(users):
    result = {}
    for user in users.keys():

        if len(users[user].keys()) != 4:
            continue

        if users[user]["started"] - users[user]["arrived"] > time_free_wait * 60:
            continue

        lateness = users[user]["finished"] - users[user]["ordered"][1] - users[user]["ordered"][2] * 60 - users[user]["ordered"][3] * 60 - time_free_wait * 60

        if lateness <= 0:
            continue

        if user not in result:
            result[users[user]["ordered"][0]] = lateness
        else:
            result[users[user]["ordered"][0]] += lateness

    return result


def get_sort_answer(dict_users):
    return " ".join([x[0] for x in sorted(sorted(list(dict_users.items()), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)])


number_banks = int(input().strip(" "))

for _ in range(number_banks):
    num_event, num_users, time_free_wait = [int(el) for el in input().strip(" ").split()]
    users = {}
    for _ in range(num_event):
        describe_event = input().strip(" ").split()
        event = describe_event[0]
        user = describe_event[1]

        if user not in users:
            users[user] = {}

        if event not in users[user]:
            if event == "ordered":
                users[user][event] = [describe_event[2].strip(), int(describe_event[3]), int(describe_event[4]), int(describe_event[5])]
            else:
                users[user][event] = int(describe_event[2])

    pre_res = get_result(users)

    res = get_sort_answer(pre_res)

    if res:
        print(res.strip(" "))
    else:
        print("-".strip(" "))
