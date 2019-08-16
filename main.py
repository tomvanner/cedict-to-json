from Extracter import Extracter
from Parser import Parser

test = Extracter('https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip')
data_name = test.run()


parser = Parser(data_name)
cedict = parser.parse()

print(cedict)