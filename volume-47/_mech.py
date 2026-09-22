#!/usr/bin/env python3
"""Mechanical pass for sermon cleanup: dash->comma, clump splitting, verse prefixes."""
import re, sys

fn = sys.argv[1]
t = open(fn).read()
orig = t

# 1. break up word clumps [a-z][A-Z] -> space, but not inside existing hyphenated words
t = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', t)

# 2. verse-number prefixes on exposition lines (line starts)
t = re.sub(r'^(?:\d+\s*[-–,]\s*\d+\s*(?:\.|,|;)|[12]\s+[A-Z]?\d+\s*\.)\s*', '', t, flags=re.M)
t = re.sub(r'^(\d+)\s*[.,]\s*(\d+)\s*\.\s*', r'\1, \2. ', t, flags=re.M)  # "4-6." n/a join
t = re.sub(r'^\d+\s*\.\s*', '', t, flags=re.M)
t = re.sub(r'^(?:Verses?|Verse)\s+[\d,;\- ]+\.\s*', '', t, flags=re.M)

# 3. em dashes -> comma (base; judgment cases reviewed after)
t = t.replace('&mdash;', ',')

# space after comma that was glued to following word
import re as _re
t = _re.sub(r',(?=[A-Za-z])', ', ', t)
t = _re.sub(r'"(?=, )', '"', t)

# cleanup common artifacts
t = re.sub(r',\s*,+', ', ', t)
t = re.sub(r'[ \t]{2,}', ' ', t)
t = re.sub(r' \.', '.', t)
t = re.sub(r' ,', ',', t)
t = re.sub(r'\. ,', '.', t)
t = re.sub(r'\? ,', '?', t)

open(fn, 'w').write(t)
print('changed chars:', len(orig) - len(t))