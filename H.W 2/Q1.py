import re
filename = "C:\\Users\\schta\\PycharmProjects\\research_hw1\\H.W 2\\text.txt"
filename2 = "C:\\Users\\schta\\PycharmProjects\\research_hw1\\H.W 2\\text2.txt"



def valid_email(filename):
    """
    this method get a file name with text inside it, and find all valid and invalid email addresses using 'Regular exspretions'
    :param filename:
    name of file.txt
    :return:
    1.list of valid emails
    2.list of invalid emails found in the text
    >>> valid_email(filename)
    valid email addresses:
     ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    invalid email addresses:
     ['abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']
    >>> valid_email(filename2)
    valid email addresses:
     ['barschtalman@gmail.com', 'fdsf@gmail.com']
    invalid email addresses:
     ['.bar@gmail.com', 'ba..r.@gmail.com', 'bar@.gmail.com', 'bar@gmail.c', 'moshe@maccabi.co.il.re.ol']
    """
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


if __name__ == '__main__':
    import doctest

    doctest.testmod()

