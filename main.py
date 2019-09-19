import json
from Extracter import Extracter
from Parser import Parser

# Entry point
cedict_zip = Extracter('https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip')
data_name = cedict_zip.run()

# Converts to JSON
parser = Parser(data_name)
cedict = parser.parse()
cedict_json = json.dumps(cedict, ensure_ascii=False)

# Writes JSON to local file
with open('cedict.json', 'w', encoding='utf8') as cedict_out:
    json.dump(cedict, cedict_out, ensure_ascii=False)