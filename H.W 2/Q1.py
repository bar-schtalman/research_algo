import re
filename = "C:\\Users\\schta\\PycharmProjects\\research_hw1\\H.W 2\\text.txt"


def valid_email(filename):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valids = []
    invalids = []
    f = open(filename, "r")
    for line in f:
        for word in line.split():
            if re.fullmatch(regex, word):
                valids.append(word)
            elif ('@' or '.') in word:
                invalids.append(word)
    print("valid emails addresses:\n",valids)
    print("invalid email addresses:\n",invalids)
    f.close()

valid_email(filename)

