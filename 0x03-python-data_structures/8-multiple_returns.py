#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sent_leng = len(sentence)
    else:
        sent_leng = 0
    return (sent_leng, sentence if not sentence else sentence[:1])
