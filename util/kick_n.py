#!/usr/bin/env python

#  Copyright (C) 2012 Tianyang Li
#  ty@li-tianyang.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License


"""
count the number of read (or read pair)
with N in the sequence
"""

# TODO: N distribution

from __future__ import division

import getopt
import sys
from itertools import izip

from Bio import SeqIO


def single_kick_n(s_file, fmt, fout_prefix):
    rec_count = 0
    n_count = 0
    
    with open("%s.%fmt" % (fout_prefix, fmt)) as fout:
        for rec in SeqIO.parse(s_file, fmt):
            rec_count += 1
            if "N" in str(rec.seq).upper():
                n_count += 1
            else:
                fout.write(rec.format(fmt))
            
    print >> sys.stderr, "%d/%d" % (n_count, rec_count)
    print >> sys.stderr, n_count / rec_count


def paired_kick_n(file1, file2, fmt, fout_prefix):
    pair_count = 0
    n_count = 1
    
    with open("%s_1.%s" % (fout_prefix, fmt), 'w') as fout1:
        with open("%s_2.%s" % (fout_prefix, fmt), 'w') as fout2:
            for rec1, rec2 in izip(SeqIO.parse(file1, fmt), SeqIO.parse(file2, fmt)):
                pair_count += 1
                if ("N" in str(rec1.seq).upper()) or ("N" in str(rec2.seq).upper()):
                    n_count += 1
                else:
                    fout1.write(rec1.format(fmt))
                    fout2.write(rec2.format(fmt))
            
    print >> sys.stderr, "%d/%d" % (n_count, pair_count)
    print >> sys.stderr, n_count / pair_count


def main(argv):
    opts, _ = getopt.getopt(argv, 's:1:2:f:p:', [])

    single_file = None
    pair_file_1 , pair_file_2 = None, None
    fmt = None
    fout_prefix = None

    for opt, arg in opts:
        if opt == '-s':
            single_file = arg
        if opt == '-1':
            pair_file_1 = arg
        if opt == '-2':
            pair_file_2 = arg
        if opt == '-f':
            fmt = arg
        if opt == '-p':
            fout_prefix = arg
    
    if ((not single_file 
        and (not pair_file_1
        or not pair_file_2))
        or not fout_prefix):
        print >> sys.stderr, "missing options"
        sys.exit(1)
    
    if single_file:
        single_kick_n(single_file, fmt)
        return
    
    if not pair_file_1 or not pair_file_2:
        print >> sys.stderr, "missing options"
        sys.exit(1)
    paired_kick_n(pair_file_1, pair_file_2, fmt)

