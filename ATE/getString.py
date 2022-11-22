'''
本脚本用于从ate原版源码中，剥离字符串并格式化为message或choice。
可减轻一个一个一个复制的麻烦（意味深 而可以一坨一坨复制
用法：IDLE打开（不用IDLE不方便复制）运行，将代码段放入，回车，
之后如果直接回车则输出message，键入c再回车输出choice。
输入选项时需要复制的是字符串内冒号后的内容。
用例：（“>”仅用于区别输入和输出，实际使用不会出现）
> choose = input('黑暗')
> view_status()
> choose = input('无边的黑暗')
> view_status()
> choose = input('似乎有什么东西在流动着')
> (enter)
"message": [
    "黑暗",
    "无边的黑暗",
    "似乎有什么东西在流动着"
]
> A.foo,B.bar,C.钝角
> c
"choice": ["foo", "bar", "钝角"]

之后复制输出内容到JSON代码中，建议使用VSCode，因为可以自动处理缩进。
（虽然不缩进不会影响JSON解析但是你也不想看到一拖四吧（  ）


注意：
如果提取的是output，只会提取单引号字符串，字符串长度<=3且第一个字符为ASCII字符则不会提取。
如：'A' 'ABC'

不考虑转义。形如'I\'m XXX'的字符串，请手动输入JSON文件中。
'''

import json
import re


def get(s):
    ret = []
    strings = re.findall("'(.+?)'", s)
    for each in strings:
        if len(each) > 3 or ord(each[0]) > 127:
            ret.append(each)
    return '"message": ' + json.dumps(ret, indent=4, ensure_ascii=False)


def choice(s):
    choices = []
    c = s.split(",")
    for each in c:
        choices.append(each[2:])
    return '"choice": ' + json.dumps(choices, ensure_ascii=False)

def main():
    s = ''
    while True:
        i = input()
        if i == "":
            print(get(s))
            s = ''
        elif i == "c":
            print(choice(s))
            s = ''
        else:
            s += i
        

if __name__ == "__main__":
    main()


