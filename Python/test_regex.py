import re

text = "�й����Ϻ���������Ϻ�"
regex = re.compile(r'(\w*�Ϻ�\w*)')
print regex.findall(text)
print regex.sub(lambda m: '[' + m.group(0) + ']', text)
