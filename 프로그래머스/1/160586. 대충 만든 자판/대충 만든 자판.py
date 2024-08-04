def solution(keymap, targets):
    answer = []

    set_keymap = set(''.join(keymap))
    keymap_dict = {key: -1 for key in set_keymap}

    for k in keymap:
        for s in targets:
            for i in s:
                new_index = k.find(i)
                if new_index != -1:
                    old_index = keymap_dict[i]
                    if old_index != -1 and old_index < new_index+1:
                        continue
                    keymap_dict[i] = new_index + 1

    for t in targets:
        total_count = 0
        for i in t:
            if i in keymap_dict.keys():
                total_count += keymap_dict[i]
            else:
                total_count = -1
                break
        answer.append(total_count)
                      
    return answer