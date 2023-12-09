import json
import collections
a = 0
with open(r"C:\Users\User\Downloads\Telegram Desktop\data12пр.json") as read_file:
    lines = read_file.readline()
    data = json.loads(lines)
for item in data['events_data']:
    col = collections.Counter()
    if item["client_id"] == 62602 and item["category"] == 'page':
        a+=1
        print(item)
print("Количество запросов клиента 62602 в категории 'page':", a)



