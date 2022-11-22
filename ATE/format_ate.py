'''
deprecated
用于在游玩中将发出的信息格式化json数组。
已弃用。
'''
import json

def to_json_array(string: str):
    return json.dumps(string.split("\n"), indent=4)



