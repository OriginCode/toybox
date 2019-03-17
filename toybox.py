'''
This file is for importing
'''

# counter.py
import yaml
from pathlib import Path

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

    # Traverse the dir and find the maintaining packages by reading the lilac.yaml.
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
        w = src[len(src) - x - 1]
        out = out + w
    return out