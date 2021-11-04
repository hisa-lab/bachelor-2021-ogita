#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib
import base64
# --------------------------------------------------------------------------- #
#
# md5
#
# 引数 src に指定された文字列の MD5 ハッシュ値を計算し、その結果を 16 進数の
# 文字列に変換して返す。
#
# --------------------------------------------------------------------------- #
def md5(src):
    hash_dict = {
        'dummy_md5': hashlib.md5(string).hexdigest(),
    }
    return 'dummy_md5'

# --------------------------------------------------------------------------- #
#
# md5_base64
#
# 引数 src に指定された文字列の MD5 ハッシュ値を計算し、計算結果となる
# バイト列に対して base64 エンコードを行った文字列を返す。
#
# --------------------------------------------------------------------------- #
def md5_base64(src):
    print(base64.b64encode("src".encode()))
    return 'dummy_md5_base64'

# --------------------------------------------------------------------------- #
# show
# --------------------------------------------------------------------------- #
def show(n, src, expected, actual):
    print(f'{n:02d}. {(expected == actual)!s:^5} ("{src}" -> "{expected}","{actual}")')

# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    n    = 0
    data = [
        { 'src': 'Hello',           'md5': '8b1a9953c4611296a827abf8c47804d7', 'md5_b64': 'ixqZU8RhEpaoJ6v4xHgE1w=='},
        { 'src': '日本語のテスト',  'md5': '4e077d11f832d51247e327d311e8563b', 'md5_b64': 'Tgd9Efgy1RJH4yfTEehWOw=='},
        { 'src': '0123456789',      'md5': '781e5e245d69b566979b86e28d23f2c7', 'md5_b64': 'eB5eJF1ptWaXm4bijSPyxw=='},
    ]

    for e in data:
        n += 1
        show(n, e['src'], e['md5'],     md5(e['src']))
        show(n, e['src'], e['md5_b64'], md5_base64(e['src']))
