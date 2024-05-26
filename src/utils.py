def convert_string_to_list(s):
    result = []
    for char in s:
        result.append(int(char, 16))
    return result

def convert_list_to_string(lst):
    result = ""
    for num in lst:
        result += hex(num)[2:]
    return result