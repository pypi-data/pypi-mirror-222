# -*- coding: utf-8 -*-

#
# Copyright © 2013 Charles E. Vejnar
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://www.mozilla.org/MPL/2.0/.
#

import json
import os
import re

all_exts = ['.bam', '.bedgraph', '.bin', '.bw', '.csv', '.fastq', '.json', '.log', '.pdf', '.sam', '.tab', '.txt']

def parse_fastq_filename(fname, regex=r'.+_([R,I][1,2,3])\.f'):
    m = re.match(regex, fname)
    if m:
        return m.group(1)
    else:
        return None

def get_fastqs_per_end(path_seq, paired=False, fastq_exts=None, read_regexs=None):
    if fastq_exts is None:
        fastq_exts = ['.fastq']
    if read_regexs is None:
        if paired:
            read_regexs = [r'.+_(R1)(\.f|_)', r'.+_(R2)(\.f|_)']
        else:
            read_regexs = [r'.+_(R1)(\.f|_)']
    fastqs = [[] for i in range(len(read_regexs))]
    for path, dirs, files in os.walk(path_seq, followlinks=True):
        for fname in files:
            if any([fname.endswith(e) for e in fastq_exts]):
                for i, read_regex in enumerate(read_regexs):
                    m = parse_fastq_filename(fname, read_regex)
                    if m is not None:
                        fastqs[i].append(os.path.join(path, fname))
    return fastqs

def write_report(fname, report):
    json.dump(report, open(fname+'.json', 'w'), sort_keys=True, indent=4, separators=(',', ': '))

def label2var(label):
    if label is None:
        return None
    else:
        return label.replace(' ', '_').replace('-', '_').replace('%', 'p').replace('/', '_')

def get_first_key(l, d):
    for k in l:
        if k in d:
            return d[k]
