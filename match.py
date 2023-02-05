import re

str = '/word/word2/word_3/'
# nehladal som nejaky poriadny regex na linux filepath
pare = '^/?(\w+/)+\w+/?$'
pare = '/?(\w+/)+\w+/?'

m = re.search(pare, str)
print(m.group())
