#!/usr/bin/python3

__author__ = "OriginCode"

import yaml
from pathlib import Path

USERNAME = input('Enter your GitHub username:\n')
REPO_DIR = input('Enter the repo location:\n')

# Read the repo dir.
p = Path(REPO_DIR)
l = [x for x in p.iterdir() if x.is_dir()]

# Initialize the count value.
count = 0

# Traverse the dir and find the maintaining packages by reading the lilac.yaml.
for x in range(len(l)):
    try:
        config = l[x] / "lilac.yaml"
        with config.open() as f:
            maintainers = yaml.load(f, Loader=yaml.BaseLoader)['maintainers']
        for y in range(len(maintainers)):
            m = maintainers[y]['github']
            if m == USERNAME:
                print('Package: ' + l[x].name)
                count += 1
    except FileNotFoundError:
        continue

print('Maintaining Packages: %d' % count)
