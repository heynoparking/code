import json


with open('show.json') as f:
    sss = json.load(f)
    print(sss)
    print(json.dumps(sss, indent=4))
