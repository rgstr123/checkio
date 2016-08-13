# coding: utf8


def left_join(phrases):
    lis = list(phrases)
    for x in lis:
        lis[lis.index(x)] = x.replace("right", "left")
    lis = ",".join(lis)
    return lis


# ____________________________________________________________________________
#                     Можно было проще
#
# def left_join(phrases):
#     return ",".join(phrases).replace("right", "left")
#
#
# ____________________________________________________________________________


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"