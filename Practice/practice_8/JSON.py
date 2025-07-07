import json
from pprint import pprint

with open("Practice/practice_8/json_file.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
# pprint(records)
records[1]['group_number'] = 3
with open("Practice/practice_8/json_file.json", "w", encoding="UTF-8") as file_out:
    json.dump(records, file_out, ensure_ascii=False, indent=2)