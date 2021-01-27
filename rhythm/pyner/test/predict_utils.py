#encoding:utf-8
import json
from collections import defaultdict

def format_result(result,words):
    '''
    形式调整
    :param result:
    :param words:
    :return:
    '''
    entities = defaultdict(list)
    entities['text'] = "".join(words)
    if len(result) == 0:
        entities['info'] = result
    else:
        list1=[]
        for record in result:
            begin = record['begin']
            end  = record['end']
            list1.append("".join(words[begin:end + 1]))
            list1.append(record['type'])
            # entities['info'].append({
            #     'word': ["".join(words[begin:end + 1]),record['type']]
            #
            # })
    return list1

def get_entity(path,tag_map):
    '''
    entity：B_ORG B_PER B_T
    :param path:
    :param tag_map:
    :return:
    '''
    results = []
    record = {}
    for index,tag_id in enumerate(path):
        if tag_id == 0: # 0是我们的pad label
            continue
        tag = tag_map[tag_id]
        if tag.startswith("B-"):
            if record.get('end'):
                results.append(record)
            record = {}
            record['begin'] = index
            record['type'] = tag.split('-')[1]
        elif tag.startswith('I-') and record.get('begin') != None:
            tag_type = tag.split('-')[1]
            if tag_type == record['type']:
                record['end'] = index
        else:
            if record.get('end'):
                results.append(record)
            record = {}
    return results

def test_write(data,filename,raw_text_path):
    '''
    将test结果保存到文本中，这里是以json格式写入
    :param data:
    :param filename:
    :param raw_text_path:
    :return:
    '''
    with open(raw_text_path,'r',encoding='utf-8') as fr,open(filename,'w',encoding='utf-8') as fw:
        for text,result in zip(fr.readlines(),data):
            words = text.split()
            record = format_result(result,words)
            fw.write(''.join(record))
            fw.write('\n')
            # encode_json = json.dumps(record,ensure_ascii=False)
            # print(json.loads(encode_json))
            # print(encode_json, file=fw)
