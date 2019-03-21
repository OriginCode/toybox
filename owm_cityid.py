#!/usr/bin/python3

__author__ = "OriginCode"

import json
import gzip
import requests

def update():
    d = {}
    
    # Recommended: Manually download the file below, and put it in this folder.
    # src = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz').content
    # with open('./city.list.json.gz', 'w') as f:
    #     f.write(src)
    with gzip.open('./city.list.json.gz') as f:
        j = json.loads(f.read())
    for x in range(len(j)):
        d.update({j[x]['name']: j[x]['id']})
    out = json.dumps(d, sort_keys=True, indent=4)
    with open('./city2id.json', 'w') as f:
        f.write(out)

def main():
    with open('./city2id.json') as f:
        j = json.load(f)
    src = input('Enter a city name to get the ID on openweathermap.org. Or enter \'update\' to update the database.\n> ')
    if src == 'update':
        update()
        main()
    else:
        print(j[src])

if __name__ == "__main__":
    main()