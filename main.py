# How to merge two JSON objects in Python

import json

obj1 = json.dumps({'id': 1, 'name': 'bobby hadz'})
obj2 = json.dumps({'site': 'bobbyhadz.com', 'topic': 'Python'})

dict1 = json.loads(obj1)
dict2 = json.loads(obj2)

merged_dict = {**dict1, **dict2}

# 👇️ {'id': 1, 'name': 'bobby hadz', 'site': 'bobbyhadz.com', 'topic': 'Python'}
print(merged_dict)