from pypinyin import lazy_pinyin
def translate(text):
    pinyin_list =lazy_pinyin(text) # 返回拼音列表 [ 'ni', 'hao', 'shi', 'jie' ]
    pinyin_string = "".join(pinyin_list) # 连接成字符串
    return pinyin_string