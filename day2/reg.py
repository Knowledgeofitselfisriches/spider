# _*_ coding:utf-8 _*_
import re

text = 'hello jack, hello rose'


def text_regex():
    rule = r'(\w+) (\w+)'
    pattern = re.compile(rule, re.I)
    result = pattern.sub('hello', text)
    print(result)


def fun(args):
    return 'hi ' + args.group(2)


def text_sub():
    rule = r'(\w+) (\w+)'
    pattern = re.compile(rule, re.I)
    result = pattern.sub(fun, text)
    print(result)


if __name__ == "__main__":
    text_sub()