import re
filename = "C:\\Users\\schta\\PycharmProjects\\research_hw1\\H.W 2\\text4.txt"


def valid_email(filename):
    regex = r'\b([A-Za-z\d]+[._%+-])*([A-Za-z\d])+@([A-Za-z\d-])+\.([A-Z|a-z]{2,})\b'
    valid = []
    invalids = []
    f = open(filename, "r")
    for line in f:
        for word in line.split():
            if re.fullmatch(regex, word):
                valid.append(word)
            elif ('@' or '.') in word:
                invalids.append(word)
    print("valid email addresses:\n",valid)
    print("invalid email addresses:\n",invalids)
    f.close()


valid_email(filename)

