import sys, json, pprint

path = '/home/coventry/bernie/outreach/'
if path not in sys.path:
    sys.path.append(path)

from gobernie import query

q = {'RESIDENTIAL_ZIP': '45349',
     'FIRST_NAME': 'JOHN',
     'LAST_NAME': 'LEWIS',
     }

for result in query.search(q):
    pprint.pprint(result)
