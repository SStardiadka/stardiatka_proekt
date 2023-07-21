import re


def decodeString(string: str) -> str:
    """
    Привети строку типа 10[a2[c]] к виду
    accaccaccaccaccaccaccaccaccacc
    число * [строка]
    """
    result = re.sub(r"(\d+)\[(\w+)\]", lambda m: int(m[1]) * m[2], string)
    if "[" in result:
        return decodeString(result)
    return result


strin = "10[a2[c]]"
print(decodeString(strin))
