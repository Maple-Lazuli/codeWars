def to_jaden_case(string):
    strList = str.split(string, sep=" ")
    cappedList = []
    for x in strList:
        cappedList.append(str.upper(x[0]) + x[1:])
    return " ".join(cappedList)

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
