def compressString(s: str) -> str:
    prevChar: str = s[0]
    prevCt        = 1
    result: str   = ""

    i = 1
    while i < len(s):
        if s[i] == prevChar:
            prevCt +=1 
        else:
            result = result + prevChar + str(prevCt)
            prevCt = 1
        prevChar = s[i]
        i+=1
    result = result + prevChar + str(prevCt)
  
    return result if len(result) < len(s) else s


s = input("Enter a string to compress: ")
print("result: " + str(compressString(s)))