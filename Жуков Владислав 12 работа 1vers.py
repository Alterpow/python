import json
import collections
a = 0
with open(r"C:\Users\User\Downloads\Telegram Desktop\data12пр.json") as read_file:
    lines = read_file.readline()
    data = json.loads(lines)
a = collections.Counter()
b = {}
c = {}
count = 0
for lists in data["events_data"]:
    b = dict(zip(lists.keys(), lists.values()))
    count += 1
    if b["client_id"] == 62602 and b["category"] == 'page':
        for word in b:
            a[word] +=1
print(a)
    

    

