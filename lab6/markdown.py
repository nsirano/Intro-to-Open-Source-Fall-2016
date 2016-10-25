"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter,
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertCode(line):
    line = re.sub(r'`(.*)`', r'<code>\1</code>', line)
    return line

def convertH(line):
    for h in range(6,0,-1):
        if re.match(r'^[\s|>]*[#]{%d}[\s]+.*'%(h), line):
            prefix = re.sub(r'^([\s|>]*).*', r'\1', line)
            if re.match(r'^[\s]*$', prefix):
                prefix = re.sub(r'(.*)', r'', prefix)

            parsed_line = re.sub(r'^[\s|>]*[#]{%d}[\s]+(.*)'%h, r'\1', line)
            line = re.sub(r'(.*)', r'%s<h%d>\1</h%d>'%(prefix,h,h), parsed_line)
    return line

def convertBlockquote(line):
    quotes = 0
    while re.match(r'^[\s]*>.*', line):
        quotes += 1
        line = re.sub(r'^[\s]*>[\s]*(.*)', r'\1', line)

    line = re.sub(r'(.*)',
                  r'%s\1%s'%('<blockquote>'*quotes,'</blockquote>'*quotes),line)
    return line

for line in fileinput.input():
    line = line.rstrip()
    line = convertStrong(line)
    line = convertEm(line)
    line = convertCode(line)
    line = convertH(line)
    line = convertBlockquote(line)
    print '<p>' + line + '</p>',
