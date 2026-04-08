#№5
reversetext = "Hello world!"

def reversestring(text):
    result = ""
    word = ""
    for char in text:
        word = char + word
    
    result = word
    return result

finalresult = reversestring(reversetext)
print(finalresult)
