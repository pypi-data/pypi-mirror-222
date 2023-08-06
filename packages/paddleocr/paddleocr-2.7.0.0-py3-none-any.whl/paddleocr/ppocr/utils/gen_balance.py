import numpy
import json

def save_corpus(corpus, similar):
    f = open(corpus, "r")
    samples = f.readlines()
    similar = open(similar, "r")
    all_dict = {}
    for line in similar.readlines():
        for k,v in json.loads(line):
            if k not in all_dict:
                all_dict[k] = v



