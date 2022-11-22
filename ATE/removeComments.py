'''
本脚本用于移除jsonc文件注释。
用法：直接在文件管理器中双击（若使用vscode需先保存jsonc文件）。
警告：本脚本忽略了字符串内出现/*或//的情况，（懒
故将认定其为注释。请不要在jsonc字符串中添加会被误认为注释的内容！
'''


import re

def main():
    with open("data.jsonc","r", encoding="utf-8") as jsonc_file:
        jsonc = jsonc_file.read()

    processed = re.sub("/\*.*?\*/","",re.sub("//.*?\n", "\n", jsonc))
    with open("data.json", "w+", encoding="utf-8") as json_file:
        json_file.write(processed)
    with open("json.js", "w+", encoding="utf-8") as json_file:
        json_file.write("window.ateData = " + processed)

if __name__ =="__main__":
    main()




