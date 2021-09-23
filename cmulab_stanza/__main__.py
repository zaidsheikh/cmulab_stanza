#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from .model import get_results

if __name__ == "__main__":
   print(get_results(sys.argv[1]))
