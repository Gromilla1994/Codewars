def solution(s):
    my_list = []
    result = s if len(s) % 2 == 0 else f"{s}_"

    for i in range(len(result), sep=2):
        my_list.append(result[i:i+2])
    return my_list
