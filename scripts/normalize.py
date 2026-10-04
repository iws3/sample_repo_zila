#!/usr/bin/env python3
"""Usage: python scripts/normalize.py marks.csv
marks.csv columns: username,day,mark   (day = 1..4, mark out of max_mark_per_day)"""
import csv, sys, collections, re
cfg = open("grading.yml").read()
max_mark = float(re.search(r"max_mark_per_day:\s*(\d+)", cfg).group(1))
weights = {int(d): float(w) for d, w in re.findall(r"day_(\d+):\s*(\d+)", cfg)}
total_w = sum(weights.values())
scores = collections.defaultdict(float)
for row in csv.DictReader(open(sys.argv[1])):
    d = int(row["day"])
    if d in weights:
        scores[row["username"]] += float(row["mark"]) / max_mark * weights[d] / total_w * 100
for u, s in sorted(scores.items(), key=lambda x: -x[1]):
    print(f"{u:25s} {s:6.2f} / 100")
