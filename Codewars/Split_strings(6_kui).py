# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

def solution(s):
    my_list = []
    result = s if len(s) % 2 == 0 else f"{s}_"

    for i in range(len(result), sep=2):
        my_list.append(result[i:i+2])
    return my_list
