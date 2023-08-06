import os
import json
import requests

import openai
# import easyocr
from paddleocr import PaddleOCR, draw_ocr
import time


# 定义ppocr文本预测函数
def ppocr_pred(img_path, lang="ch", version="mobile"):
    # 提供v4 的 mobile 和 server 两种模型,默认mobile
    if version == "mobile":
        rec_model_url = "https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_rec_infer.tar"
        det_model_url = "https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_det_infer.tar"
    elif version == "server":
        rec_model_url = "https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_rec_server_infer.tar"
        det_model_url = "https://paddleocr.bj.bcebos.com/PP-OCRv4/chinese/ch_PP-OCRv4_det_server_infer.tar"
    else:
        print("other type of ppocr is not support")

    ocr = PaddleOCR(rec_model_dir=rec_model_url, det_model_dir=det_model_url)
    result = ocr.ocr(img_path, cls=False)
    result = result[0]
    boxes = [line[0] for line in result]
    scores = [line[1][1] for line in result]
    # return only text result
    txts = [line[1][0] for line in result]
    # from PIL import Image
    # image = Image.open(img_path).convert('RGB')
    # im_show = draw_ocr(image, boxes, txts, scores, font_path='/workspace/PaddleOCR/doc/fonts/simfang.ttf')
    # im_show = Image.fromarray(im_show)
    # save_path = img_path.replace(".jpg", "_ocr.jpg")
    # im_show.save(save_path)
    all_context = " ".join(txts)
    return all_context


# 定义easyocr预测函数
def easyocr_pred(img_path):
    # 识别简体中文和英文
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    # 不返回坐标信息
    result = reader.readtext(img_path, detail=0)
    all_context = "".join(result)
    return all_context


# 定义EB的回答函数
def eb_pred(ocr_result):
    headers = {
      'content-type': 'application/json',
    }
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=24.e281f51ab101d28c9d25753676cf166a.2592000.1689752780.282335-34819751'
    post_data= {'messages': [{'role':'user','content':ocr_result}]}
    data = json.dumps(post_data)
    # 调用EB服务
    response = requests.post(url, headers=headers, data=data)
    # 打印结果
    # print(response.content)
    eb_result= json.loads(response.content)["result"]
    eb_result = eb_result.replace("```","").replace("json","")
    value = list(eval(eb_result).values())[0][0]
    return value


# 定义ChatGPT的回答函数
def chat_with_gpt(prompt):
    # api_key from yuning
    # openai.api_key = "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"
    # api_key from yehua
    # openai.api_key = "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"
    # api_key from jiangbin
    openai.api_key = "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"
    response = openai.Completion.create(
        engine='text-davinci-003',  # 指定GPT模型版本
        prompt=prompt,
        max_tokens=200,  # 控制回答的长度
        temperature=0,  # 控制回答的创造性
        n=1,  # 生成一个回答
        stop=None,  # 可以提供一个字符串作为回答的结束标记
        timeout=15,  # 请求超时时间（秒）
    )
    answer = response.choices[0].text.strip()
    print(answer)
    try:
        answer = answer.replace("：", "")
        answer = eval(answer)
        answer = list(answer.values())[0]
    except:
        answer = answer
    return answer


def cal_acc(file_name):
    all_count = 0
    correct_count = 0
    with open(file_name, "r", encoding='utf-8-sig') as f:
        for line in f.readlines():
            try:
                img_name, key, value, eb_result = line.strip("\n").split(",")
            except:
                continue
            if value == eb_result:
                correct_count += 1
            all_count += 1
    print("准确率：", correct_count / all_count)


if __name__ == "__main__":
    # result = eb_pred("请介绍你自己")
    # print(result)
    # prompt = "你现在的任务是从OCR文字识别的结果中提取我指定的关键信息。OCR的文字识别结果使用```符号包围，包含所识别出来的文字，顺序在原始图片中从左至右、从上至下。我指定的关键信息使用[]符号on格式，包含一个key-value对，key值为我指定的关键信息，value值为所抽取的结果。请只输出json格式的结果，不要包含其它多余文字！下面正式开始：```F067846 检票：22 北京南站 天津站 C2次车 始发改签 2302051998****156X裴瑜丽 买票请到12306发货请到95306 中国铁路祝您旅途愉快 10010301110403F067846 北京南售```,要抽取的关键信息是：[车票号], 请输出你的结果。"
    prompt = "请介绍你自己"
    llm_result = chat_with_gpt(prompt)
    print(llm_result)
    exit()
    ## 选择ocr预测引擎和大模型预测引擎
    ocr_engine = "ppocr"  # or easyocr
    ppocr_mode = "server"  # or sever
    llm_engine = "chatgpt"  # or chatgpt
    scene = "air_ticket"

    assert ocr_engine in ["ppocr", "easyocr"], Exception(
        f'ocr_engine not support {ocr_engine}')
    assert ppocr_mode in ["mobile", "server"], Exception(
        f'ppocr_mode not support {ppocr_mode}')
    assert llm_engine in ["chatgpt", "eb"], Exception(
        f'llm_engine not support {llm_engine}')

    # all_result = {}
    # for img_name in os.listdir(scene):
    #     if img_name.endswith("csv"):
    #         continue
    #     img_path = os.path.join(scene, img_name)
    #     # print("img path:", img_path)
    #     if ocr_engine == "ppocr":
    #         ocr_result = ppocr_pred(img_path, version=ppocr_mode)
    #     elif ocr_engine == "easyocr":
    #         ppocr_mode = None
    #         ocr_result = easyocr_pred(img_path)
    #
    #     # 将ocr预测结果存在字典中，key为图片名，value为ocr预测结果
    #     all_result[img_name] = ocr_result
    #
    # with open(f'ocr_result_{scene}.txt', 'w') as f:
    #     json.dump(all_result, f, ensure_ascii=False)

    with open(f'ppocr_result_{scene}.txt') as data_file:
        ocr_all_result = json.load(data_file)

    file_data = ""
    with open(f"{scene}/{scene}.csv", "r", encoding='utf-8-sig') as f:
        current_name = "tmp"
        for line in f.readlines():
            img_name, key, value = line.strip("\n").split(",")
            # print(key)
            txt_result = ocr_all_result[img_name]
            prompt = f"""你现在的任务是从OCR文字识别的结果中提取我指定的关键信息。OCR的文字识别结果使用```符号包围，包含所识别出来的文字，顺序在原始图片中从左至右、从上至下。我指定的关键信息使用[]符号包围。请注意OCR的文字识别结果可能存在长句子换行被切断、不合理的分词、对应错位等问题，你需要结合上下文语义进行综合判断，以抽取准确的关键信息。在返回结果时使用json格式，包含一个key-value对，key值为我指定的关键信息，value值为所抽取的结果。请只输出json格式的结果，不要包含其它多余文字！下面正式开始：```{txt_result}```,要抽取的关键信息是[{key}]。请输出你的结果"""
            # print(prompt)
            if llm_engine == "eb":
                # 使用EB服务
                llm_result = eb_pred(prompt)
            elif llm_engine == "chatgpt":
                # 使用ChatGPT服务
                llm_result = chat_with_gpt(prompt)
            # 将预测结果追加到文件中
            line = f"{img_name},{key},{value},{llm_result}\n"
            file_data += line
    with open(f"{scene}_{ocr_engine}_{ppocr_mode}_{llm_engine}_update.csv", "w", encoding="utf-8") as f:
        f.write(file_data)

    cal_acc(f"{scene}_{ocr_engine}_{ppocr_mode}_{llm_engine}_update.csv")

