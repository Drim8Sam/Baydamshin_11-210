request_count = int(input())
base_nicknames = dict()


def check_for_changed_nickname(base, nickname):
    global key
    if bool(base.keys()):
        for key in base.keys():
            if base[key] == nickname:
                return True, key
        return False, key
    else:
        return False, nickname


for count in range(request_count):
    request = input().split()
    old_nickname = request[0]
    new_nickname = request[1]

    if old_nickname not in base_nicknames.keys():
        check_result = check_for_changed_nickname(base_nicknames, old_nickname)
        if check_result[0]:
            base_nicknames[check_result[1]] = new_nickname

        else:
            base_nicknames[old_nickname] = new_nickname
    else:
        base_nicknames[old_nickname] = new_nickname


print(len(base_nicknames.keys()))

for key, value in base_nicknames.items():
    print(key, value)

    
