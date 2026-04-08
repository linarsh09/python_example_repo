#3-variant
def remote_str(s):
    
    result = ""

    for char in s:
        if char not in result:
            
            result += char

    return result

s = input()
print(remote_str(s))


