#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if (len(sentence)) == 0:
            first_chr = None
        else:
            first_chr = sentence[0]
            length = len(sentence)
    tuples = (length, first_chr)
    return (tuples)
