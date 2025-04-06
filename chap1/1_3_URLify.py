''' URLify: replace spaces with %20
'''


def toUrl(s: list[str], strLength: int) -> str:
    i = strLength - 1
    j = len(s) - 1
    while i >= 0 and j >= 0:
        if s[i] != ' ':
            s[j] = s[i]
            j -= 1
        else:
            s[j] = '0'
            s[j-1] = '2'
            s[j-2] = '%'
            j -= 3
        i -= 1
    return "".join(s)


name = list("Mr John Smith    ")
trueLength = 13
print("original string:\t" + "".join(name))
print("urlified:\t\t" + toUrl(name, trueLength))
