# coding:utf-8
import paddle
import paddle.fluid as fluid
import numpy as np

def gen_dict(st_name, dy_name):
    st_file = open(st_name, "r")
    dy_file = open(dy_name, "r")

    st_lines = []
    dy_lines = []
    dict1 = {}

    for line in st_file.readlines():
        #print(line)
        #exit()
        st_lines.append(str(line.replace('\n', '')))

    for line in dy_file.readlines():
        dy_lines.append(line.replace('\n', ''))

    for i, item in enumerate(st_lines):
        dict1[item] = dy_lines[i]
    print(dict1)
    return dict1

def change_param(origin_param, target_param, name_dict):
    st_param = np.load(origin_param)
    dy_dict = dict()
    for k,v in st_param.items():
        dy_dict[name_dict[k]] = v
    np.savez("dy_init_param_dict.npz", **dy_dict)

def check_param(target_param):
    dy_param = np.load(target_param)
    for k,v in dy_param.items():
        print(k)
if __name__ == "__main__":
    #name_dict = gen_dict("st_param.txt", "dy_param.txt")
    #change_param('st_init_param_dict.npz', 'dy_init_param_dict.npz', name_dict)
    #check_param('dy_param.npz')
    # import cv2
    # import numpy as np
    # from PIL import ImageFont, Image, ImageDraw
    # import arabic_reshaper
    # from bidi.algorithm import get_display
    #
    # white_bg = np.ones((32, 100, 3)) * 255
    # text_img = Image.fromarray(np.uint8(white_bg))
    # draw = ImageDraw.Draw(text_img)
    # #text = "الكبرى"
    # text = "ﺏﺎﻘﻃﺎﻳﺍ"
    # print(text)
    # exit()
    # reshaped = arabic_reshaper.reshape(u"%s" % text)
    # bidi = get_display(reshaped)
    #
    # font = ImageFont.truetype("../train_data/ArabicUIDisplay.ttc", 20)
    # draw.text((0, 0), bidi, fill="red", font=font)
    # #print(text_img)
    # #out = out.astype(np.int32)
    # out = np.array(text_img)
    # cv2.imwrite("arabic.jpg", out[:,:,::-1])

    from paddleocr import PaddleOCR, draw_ocr

    # 同样也是通过修改 lang 参数切换语种
    ocr = PaddleOCR(lang="japan")  # 首次执行会自动下载模型文件
    img_path = './doc/imgs/japan_2.jpg'
    result = ocr.ocr(img_path)
    # 打印检测框和识别结果
    for line in result:
        print(line)

    # 可视化
    from PIL import Image

    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    draw_img = draw_ocr(
        image,
        boxes,
        txts,
        scores,
        drop_score=0.5,
        font_path='./doc/fonts/japan.ttc')
    im_show = Image.fromarray(draw_img)
    im_show.save('result.jpg')
