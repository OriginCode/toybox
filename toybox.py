# This file is for importing

# counter.py
import yaml
from pathlib import Path

# owm_cityid.py
import json
import gzip
import requests

__author__ = "OriginCode"

def addspace(src):
    out = ""
    for x in range(len(src)):
        out = out + src[x] + " "
    out = out[0:len(out) - 1]
    return out

def counter(username, repo_dir):
    # Read the repo dir.
    p = Path(repo_dir)
    l = [x for x in p.iterdir() if x.is_dir()]

    # Initialize the count value.
    count = 0

    # Traverse the dir and find the maintaining packages.
    for x in range(len(l)):
        try:
            config = l[x] / "lilac.yaml"
            with config.open() as f:
                maintainers = yaml.load(f)['maintainers']
            pkgs = []
            for y in range(len(maintainers)):
                m = maintainers[y]['github']
                if m == username:
                    pkgs.append(l[x].name)
                    count += 1
        except FileNotFoundError:
            continue

    return pkgs, count

def inverting(src):
    out = ""
    for x in range(len(src)):
        out = out + src[len(src) - x - 1]
    return out

class owm_cityid:
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
    
    def search(src):
        with open('./city2id.json') as f:
            j = json.load(f)
        return j[src]