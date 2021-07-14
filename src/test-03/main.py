#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- #
#
# hash
#
# 引数 src に指定された文字列を引数 kind で指定された種類のハッシュ関数を用いて
# 計算し、その結果を文字列で返します。 返り値は、引数 base64 が true の場合は
# Base64 エンコードされた結果、false の場合は 16 進数表記です。
#
# --------------------------------------------------------------------------- #
def hash(src, kind, base64):
    return 'dummy_base64' if base64 else 'dummy_hex'

# --------------------------------------------------------------------------- #
# show
# --------------------------------------------------------------------------- #
def show(n, src, kind, expected, actual):
    print(f'{n:02d}. {(expected == actual)!s:^5} ({kind}: "{src}" -> "{expected}","{actual}")')

# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    n    = 0
    data = [
        { 'src': 'Hello', 'kind': 'md5', 'hex': '8b1a9953c4611296a827abf8c47804d7', 'base64': 'ixqZU8RhEpaoJ6v4xHgE1w==' },
        { 'src': 'Hello', 'kind': 'sha1', 'hex': 'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0', 'base64': '9/+ei3uy4Jtwk1pdeF4MxdnQq/A=' },
        { 'src': 'Hello', 'kind': 'sha256', 'hex': '185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969', 'base64': 'GF+NsyJx/iX1Yab8k4suJkMG7DBO2lGAB9F2SCY4GWk=' },
        { 'src': '日本語のテスト', 'kind': 'md5', 'hex': '4e077d11f832d51247e327d311e8563b', 'base64': 'Tgd9Efgy1RJH4yfTEehWOw==' },
        { 'src': '日本語のテスト', 'kind': 'sha1', 'hex': '10cc4bd729a80d971a8ce8594392caac9c478ad1', 'base64': 'EMxL1ymoDZcajOhZQ5LKrJxHitE=' },
        { 'src': '日本語のテスト', 'kind': 'sha256', 'hex': 'ee82542eb4903b0bfa0a60e3ed8a9a60550475aaf9ffee23d5f94060f9017861', 'base64': '7oJULrSQOwv6CmDj7YqaYFUEdar5/+4j1flAYPkBeGE=' },
        { 'src': '0123456789', 'kind': 'md5', 'hex': '781e5e245d69b566979b86e28d23f2c7', 'base64': 'eB5eJF1ptWaXm4bijSPyxw==' },
        { 'src': '0123456789', 'kind': 'sha1', 'hex': '87acec17cd9dcd20a716cc2cf67417b71c8a7016', 'base64': 'h6zsF82dzSCnFsws9nQXtxyKcBY=' },
        { 'src': '0123456789', 'kind': 'sha256', 'hex': '84d89877f0d4041efb6bf91a16f0248f2fd573e6af05c19f96bedb9f882f7882', 'base64': 'hNiYd/DUBB77a/kaFvAkjy/Vc+avBcGflr7bn4gveII=' }        
    ]

    for e in data:
        n += 1
        show(n, e['src'], e['kind'], e['hex'], hash(e['src'], e['kind'], False))
        n += 1
        show(n, e['src'], e['kind'], e['base64'], hash(e['src'], e['kind'], True))
