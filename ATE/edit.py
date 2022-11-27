import re

def read(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def write(file, text):
    with open(file, "w+", encoding="utf-8") as f:
        return f.write(text)

tags = ["nosolo", "nolts"]


def solo(lts):
    result = []
    curcode = ""
    curcomment = ""
    linecomment = False
    cache = False
    for char in read("ATE.js"):
        if curcomment:
            if char == "*":
                cache = True
            elif cache and char == "/":
                cache = False
                if "#nosolo" in curcomment:
                    result.append(10)
                elif "#nolts" in curcomment:
                    result.append(20)
                elif "#endnosolo" in curcomment:
                    result.append(11)
                elif "#endnolts" in curcomment:
                    result.append(21)
                elif "#soloonly" in curcomment and (lts or "#ltsonly" not in curcomment):
                    print(curcomment)
                    result.append(re.search("\\{(.+)\\}", curcomment, flags=re.S)[1])
                curcomment = ""
            elif cache:
                curcomment += "*" + char
                cache = False
            else:
                curcomment += char
        else:
            if linecomment:
                curcode += char
                if char == "\n":
                    linecomment = False
                continue
            if cache and char == "/":
                curcode += "//"
                linecomment = True
                cache = False
            elif char == "/":
                cache = True
            elif cache and char == "*":
                result.append(curcode)
                curcomment = "/*"
                curcode = ""
                cache = False
            elif cache:
                curcode += "/" + char
                cache = False
            else:
                curcode += char
    output = ""
    index = 0
    l = len(result)
    print(result)
    while index < l:
        each = result[index]
        if each == 10:
            while result[index] != 11:
                index += 1
        elif each == 20 and lts:
            while result[index] != 21:
                index += 1
        elif type(each) is str:
            output += each
        index += 1
    write("ATESolo.js" if lts else "ATEBeta.js", output)



def lts():
    result = []
    curcode = ""
    curcomment = ""
    linecomment = False
    cache = False
    for char in read("ATE.js"):
        if curcomment:
            if char == "*":
                cache = True
            elif cache and char == "/":
                cache = False
                if "#nosolo" in curcomment:
                    result.append(10)
                elif "#nolts" in curcomment:
                    result.append(20)
                elif "#endnosolo" in curcomment:
                    result.append(11)
                elif "#endnolts" in curcomment:
                    result.append(21)
                elif "#ltsonly" in curcomment:
                    result.append(re.search("\\{(.+)\\}", curcomment, flags=re.S)[1])
                curcomment = ""
            elif cache:
                curcomment += "*" + char
                cache = False
            else:
                curcomment += char
        else:
            if linecomment:
                curcode += char
                if char == "\n":
                    linecomment = False
                continue
            if cache and char == "/":
                curcode += "//"
                linecomment = True
                cache = False
            elif char == "/":
                cache = True
            elif cache and char == "*":
                result.append(curcode)
                curcomment = "/*"
                curcode = ""
                cache = False
            elif cache:
                curcode += "/" + char
                cache = False
            else:
                curcode += char
    output = ""
    index = 0
    l = len(result)
    while index < l:
        each = result[index]
        if each == 20:
            while result[index] != 21:
                index += 1
        elif type(each) is str:
            output += each
        index += 1
    write("ATELTS.js", output)

def main():
    solo(False)
    solo(True)
    lts()

if __name__ == "__main__":
    main()

