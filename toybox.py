# This file is for importing

__author__ = "OriginCode"

# counter.py
import yaml
from pathlib import Path

# eqgen.py
import random

# owm_cityid.py
import json
import gzip
import requests

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
    pkgs = []

    # Traverse the dir and find the maintaining packages.
    for x in range(len(l)):
        try:
            config = l[x] / "lilac.yaml"
            with config.open() as f:
                maintainers = yaml.load(f)['maintainers']
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

def eqgen(a, b, c):    # Usage: a for the maximum num in the equation, b for the maximum result, c for how many results to return.
    l = []
    r = []
    for x in range(1, a + 1):
        for y in range(1, a + 1):
            if x + y <= b:
                l.append(str(x) + ' + ' + str(y))

    for i in range(c):
        r.append(l[random.randrange(len(l) - 1)])
    
    return r

def accelerator(src):
    out = ""
    for x in range(len(src)):
        out = out + src[x] + " " * (x + 1)
        out = out[0:len(out) - x - 1]
    return out
