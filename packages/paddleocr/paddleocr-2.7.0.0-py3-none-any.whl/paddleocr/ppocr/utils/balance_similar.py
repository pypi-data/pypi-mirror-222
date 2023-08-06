import numpy as np
import json
import random
import xlwt


def get_unbanlance_voc(path):
    result_dict = {}
    save_res = False
    unbanlance_dict = xlwt.Workbook()
    new_sheet = unbanlance_dict.add_sheet("unbanlance_char")
    i = 1
    new_sheet.write(0, 0, "char_less")
    new_sheet.write(0, 1, "count")
    new_sheet.write(0, 2, "char_more")
    new_sheet.write(0, 3, "count")
    with open(path,"r") as f:
        for line in f.readlines():
            if "txt" in line:
                continue
            label = json.loads(line)
            for key,value in label.items():
                if value < max(label.values())/2 or (max(label.values()) - value > 10000):
                    save_res = True
                    result_dict[key] = (value,max(label.values()))
                    new_sheet.write(i, 0, str(key))
                    new_sheet.write(i, 1, int(value))
                    max_value = max(label.values())
                    max_key = max(label, key=label.get)
                    new_sheet.write(i, 2, str(max_key))
                    new_sheet.write(i, 3, int(max_value))
                    i += 1
                elif value < 200:
                    save_res = True
                    result_dict[key] = value
                    new_sheet.write(i, 0, str(key))
                    new_sheet.write(i, 1, int(value))
                    i += 1
    unbanlance_dict.save(r"unbalance_freq.xls")
    return result_dict

def merge_similar_dict(path):
    f_out = open("merge_similar_dict.txt", "w")
    merge_similar_dict = {}
    with open(path, "r") as f:
        for line in f.readlines():
            if "txt" in line:
                continue
            label = json.loads(line)
            for key, value in label.items():
                if key not in merge_similar_dict:
                    merge_similar_dict[key] = value
                else:
                    merge_similar_dict[key] += value
    #with open("cy_similar.txt", "r") as f:
    with open("cy_similar_500.txt", "r") as f:
        for line in f.readlines():
            word = line.strip().strip("\n").strip(" ").strip("\t")
            line = {}
            for s in word:
                try:
                    line[s] = merge_similar_dict[s]
                except:
                    if s != " ":
                        line[s] = 0
                        print(s)
            f_out.write(json.dumps(line, ensure_ascii=False) + "\n")
    return merge_similar_dict


def get_sample(char_dict):
    corpus = open("seldom.txt", "r")
    f_out = open("new_seldom.txt", "w")
    data = corpus.readlines()
    # 移除换行符、首尾空格
    data = map(lambda l: l[:-1].split("\t")[-1].strip(), data)
    data = ''.join(data)
    for key,value in char_dict.items():
        if isinstance(value, int):
            single_less = True
            max_value = 200
        else:
            max_value = value[1]/5
        for i in range(int(max_value)):
            try:
                start_index = random.randint(0,100)
                indx = data.find(key, start_index)
            except:
                indx = data.find(key, 0)
            length = random.randint(1,6)
            add_char = data[indx:indx+length]
            f_out.write(add_char+"\n")
    f_out.close()



if __name__ == "__main__":
    result_dict = merge_similar_dict("result_similar_count.txt")
    result_dict = get_unbanlance_voc("merge_similar_dict.txt")
    #get_sample(result_dict)

