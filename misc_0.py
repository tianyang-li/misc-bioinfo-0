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

import sys

import util.count_n as count_n
import util.kick_n as kick_n

def main():
    if not sys.argv[1:]:
        print >> sys.stderr, "missing command"
        sys.exit(1)
    if sys.argv[1] == 'count_n':
        count_n.main(sys.argv[2:])
    elif sys.argv[1] == 'kick_n':
        kick_n.main(sys.argv[2:])
    
if __name__ == '__main__':
    main()    
