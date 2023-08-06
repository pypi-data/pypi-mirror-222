# -*- coding: UTF-8 -*-
# @Time:  12:57
# @Author: 파도가솨
# @File: gg.py
# @Software: PyCharm

import binascii

en_Langsa = {
    '0': '파도파도파도파도',
    '1': '파도파도파도가솨',
    '2': '파도파도가솨파도',
    '3': '파도파도가솨가솨',
    '4': '파도가솨파도파도',
    '5': '파도가솨파도가솨',
    '6': '파도가솨가솨파도',
    '7': '파도가솨가솨가솨',
    '8': '가솨파도파도파도',
    '9': '가솨파도파도가솨',
    'a': '가솨파도가솨파도',
    'b': '가솨파도가솨가솨',
    'c': '가솨가솨파도파도',
    'd': '가솨가솨파도가솨',
    'e': '가솨가솨가솨파도',
    'f': '가솨가솨가솨가솨'
}
de_Langsa = {
    '파도파도파도파도': '0',
    '파도파도파도가솨': '1',
    '파도파도가솨파도': '2',
    '파도파도가솨가솨': '3',
    '파도가솨파도파도': '4',
    '파도가솨파도가솨': '5',
    '파도가솨가솨파도': '6',
    '파도가솨가솨가솨': '7',
    '가솨파도파도파도': '8',
    '가솨파도파도가솨': '9',
    '가솨파도가솨파도': 'a',
    '가솨파도가솨가솨': 'b',
    '가솨가솨파도파도': 'c',
    '가솨가솨파도가솨': 'd',
    '가솨가솨가솨파도': 'e',
    '가솨가솨가솨가솨': 'f'
}


# 파도가솨进制编码
def encode(text):
    # 将字符串转换为16进制（字符串可含汉字）
    text16 = text.encode("utf-8").hex()
    for i in en_Langsa:
        text16 = text16.replace(i, en_Langsa[i])
    encode_text = text16
    return encode_text


# 파도가솨进制解码
def decode(text):
    text16=''
    for i in range(0, len(text), 8):
        text16 = text16 + de_Langsa[text[i:i + 8]]
    decode_text = binascii.a2b_hex(text16).decode()
    return decode_text
