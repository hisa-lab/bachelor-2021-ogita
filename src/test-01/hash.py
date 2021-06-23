#!/usr/bin/python
# -*- coding: utf-8 -*-


import hashlib


def calc_hash(string):
    u'''入力文字列のハッシュ値を求めて辞書型で出力する'''
    hash_dict = {
        'md5': hashlib.md5(string).hexdigest(),
        'sha1': hashlib.sha1(string).hexdigest(),
        'sha224': hashlib.sha224(string).hexdigest(),
        'sha256': hashlib.sha256(string).hexdigest(),
        'sha384': hashlib.sha384(string).hexdigest(),
        'sha512': hashlib.sha512(string).hexdigest(),
    }
    return hash_dict

if __name__ == '__main__':
    import sys
    string = sys.argv[1]
    hash_dict = calc_hash(string.encode('utf-8'))
    for key, value in hash_dict.items():
        print ('%s\t%s' % (key, value))