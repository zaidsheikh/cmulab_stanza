#!/usr/bin/env python
# -*- coding: utf-8 -*-

import stanza

stanza.download('en')
nlp = stanza.Pipeline('en')


def get_results(input_file):
   return nlp(input_file)
