import re

text = "中国的上海，世界的上海"
regex = re.compile(r'(\w*上海\w*)')
print regex.findall(text)
print regex.sub(lambda m: '[' + m.group(0) + ']', text)
