#!/usr/bin/env python3
"""FREE DEMO — what a pre-submission field check looks like.

Runs against a tiny SAMPLE field list (sample_fields.csv, 10 example
rows — illustrative only, not platform data). It demonstrates the two
checks that burn the most beginner simulations on WorldQuant BRAIN:

  1. a field name that does not exist (typo / wrong account) is caught
     BEFORE you simulate;
  2. a VECTOR field used without vec_avg(...) is caught too.

The full toolkit does this against the real field catalog of YOUR OWN
BRAIN account (any region / universe), and adds a local
self-correlation screen against your submitted alphas.

Usage: python3 demo_check.py
"""
import csv
import json
import re

NON_FIELDS = {
    "rank", "zscore", "group_rank", "ts_rank", "ts_zscore", "ts_mean",
    "ts_delta", "ts_backfill", "vec_avg", "signed_power", "trade_when",
    "subindustry", "industry", "sector", "market", "std",
}
TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def vec_avg_spans(expr):
    spans = []
    for m in re.finditer(r"vec_avg\s*\(", expr):
        start, depth, i = m.end(), 1, m.end()
        while i < len(expr) and depth:
            depth += {"(": 1, ")": -1}.get(expr[i], 0)
            i += 1
        spans.append((start, i - 1))
    return spans


def main():
    fields = {}
    with open("sample_fields.csv") as f:
        for row in csv.DictReader(f):
            fields[row["id"]] = row["type"]
    cands = json.load(open("candidates_sample.json"))
    for c in cands:
        expr = c["expression"]
        used = sorted({t for t in TOKEN.findall(expr) if t not in NON_FIELDS})
        spans = vec_avg_spans(expr)
        problems = []
        for name in used:
            if name not in fields:
                problems.append(f"NOT_IN_CATALOG:{name}")
            elif fields[name] == "VECTOR":
                pos = expr.find(name)
                if not any(a <= pos <= b for a, b in spans):
                    problems.append(f"VECTOR_WITHOUT_VEC_AVG:{name}")
        status = "PASS" if not problems else "FAIL"
        print(f"{c['id']}: {status} problems={problems}")


if __name__ == "__main__":
    main()
