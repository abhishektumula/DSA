def encode(message : str) -> str:
    encodedMsg = ""
    tokens = message.split(" ")
    for each in tokens:
        encodedMsg += each[::-1] + " "

    return encodedMsg.strip()

def decode(code : str) -> str:
    original = ""
    tokens = code.split(" ")
    for each in tokens:
        original += each[::-1] + " "

    return original.strip()


x = encode('i use linux and nivm btw')
y = decode(x)
print(f"{x}\n{y}" )

