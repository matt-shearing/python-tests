import re

text= "There's a hole in my __SINGLE_NOUN__, dear __NAME__"

def mad_libs(mls):
    """:param mls: String with parts the user should fill out surrounded by double underscores
    Underscores cannot be inside hint, eg, no __hint_hint__ only __hint__"""

    hints = re.findall("__.*?__", mls)

    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)

        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)