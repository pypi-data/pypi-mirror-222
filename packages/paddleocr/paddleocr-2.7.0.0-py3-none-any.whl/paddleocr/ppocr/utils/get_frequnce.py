import argparse
import os
import glob
from collections import defaultdict

import numpy as np

def analyze_labels(path: str):
    char_count_dict = defaultdict(int)

    with open(path, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        # 移除换行符、首尾空格
        data = map(lambda l: l.split("\t")[-1][:-1].strip(), data)
        data = ''.join(data)
        total_chars_count = len(data)

        for c in data:
            char_count_dict[c] += 1

    return char_count_dict, total_chars_count


def process_dir(label_dir, log=False):
    label_paths = glob.glob(label_dir + '/*.txt')
    similar_voc = open("similar_voc.txt", "r")
    f_out = open("result_similar_count.txt", "w")
    for p in label_paths:
        ratio = 1.0
        if "rec_all_fix.txt" in p:
            ratio = 0.029
        if "hard_vertical_img_list" in p:
            ratio = 0.05
        if "ch_label_0" in p:
            ratio = 0.56
        if "unlabeled_train_list_82.4_shuaku_score_0.95" in p:
            ratio = 0.062
        if "rec_caibao_fileter_eng-score_filter_illegal_month_merge_0.95" in p:
            ratio = 0.08
        if "seldom.txt" in p:
            ratio = 0.011
        name = p.split('/')[-1].split('.')[0]
        chars_count_dict, total_chars_count = analyze_labels(p)
        if ratio != 1.0:
            for k,v in chars_count_dict.items():
                chars_count_dict[k] = int(v*ratio)

        for line in similar_voc.readlines():
            word = line.split(" ")
            if len(word) > 1:
                main_word = word[0]
                similar_word = word[1]
            else:
                main_word = word[0]
                similar_word = []
            tmp_line = {}
            if main_word in chars_count_dict:
                tmp_line[main_word] = chars_count_dict[main_word]
                for s in similar_word and similar_word!=[]:
                    tmp_line[s] = chars_count_dict[s]
            f_out.write(str(tmp_line)+"\n")

        chars_count_list = list(sorted(chars_count_dict.items(), key=lambda x: x[1], reverse=True))