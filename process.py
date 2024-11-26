import json

# 生成jsonl文件
all_lans = {'cs': 'Czech', 'de': 'German', 'ru': 'Russian', 'zh': 'Chinese', 'en': 'English'}

def make_jsonl(src, tgt):
    src_file_path = f"./raw_data/test.{src}-{tgt}.{src}"
    output_file_path = f"./message_data/{src}-{tgt}.jsonl"
    with open(src_file_path, 'r', encoding='utf-8') as src_file, open(output_file_path, 'w', encoding='utf-8') as jsonl_file:
        for line in src_file:
            src_sentence = line.strip()  
            entry = {
                "role": "user",
                "content": f"Translate: This is an {all_lans[src]} to {all_lans[tgt]} translation, please provide the {all_lans[tgt]} translation for this sentence. Do not provide any explanations or text apart from the translation. \n{all_lans[src]}: {src_sentence} \n{all_lans[tgt]}: "
            }
            jsonl_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

lans = ['cs', 'de', 'ru', 'zh']
for lan in lans:
    for src in [lan, 'en']:
        tgt = 'en' if src == lan else lan
        make_jsonl(src, tgt)