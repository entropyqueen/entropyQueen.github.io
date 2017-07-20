#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import datetime

template = """
---
layout: post
title: "%s"
categories: blog
excerpt:
tags: []
image:
  feature:
date: %s +0200
modified: %s +0200
---
"""

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: %s <folder> <post_title>' % sys.argv[0])
        exit(1)
    path = sys.argv[1]
    title = sys.argv[2]
    today = datetime.datetime.now().__str__().split('.')[0]
    filename = today.split(' ')[0] + '-%s.md' % title.replace(' ', '_')
    try:
        with open(os.path.join(path, filename), 'w') as f:
            f.write(template % (title, today, today))
    except Exception as e:
        print('[-] Failed to create file: %s' % e)
    else:
        print('[+] Created file: %s ' % os.path.join(path, filename))
