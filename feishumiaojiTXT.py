import re

def extract_speaker_content(speaker_id, text):
    speaker_pattern = re.compile(rf"说话人 {speaker_id}\s+([\s\S]*?)(?=说话人 \d)")
    speaker_content = re.findall(speaker_pattern, text)
    return " ".join(speaker_content)

# 读取D盘中的'speech.txt'文件
with open("D:/speech.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 提取“说话人 1”的内容
speaker_1_content = extract_speaker_content(1, text)

# 将提取的内容保存到D盘的'speechfinish.txt'文件中
with open("D:/speechfinish.txt", "w", encoding="utf-8") as output_file:
    output_file.write(speaker_1_content)