def decode_string(message : str) -> str:
    original = ""
    words = message.split(" ")
    for each in words:
        original += each[::-1]
        original += " "

    return f"{original.rstrip()}"

def encode_string(words : str) -> str:
    res = ""
    word = words.split(" ")
    for each in word:
        res += each[::-1]
        res += " "
    n = decode_string(res)
    return f"{res.rstrip()}<--\n{n}"

print(encode_string("Sanjana aunty is very lazy"))



