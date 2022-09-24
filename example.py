import json
# data = json.load('./data.json')
# print(data)
d = None
with open("./data.json", "r") as to:
    d = json.load(to)
    # i = json.loads(d)
    # print(d)
    for i in d:
        d[i] = i
with open("to.json", "w", encoding='utf-8') as to:
    json.dump(d, to, ensure_ascii=False, indent=4)