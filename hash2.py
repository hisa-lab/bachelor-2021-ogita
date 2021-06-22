# モジュールをインポートします
import hashlib

# バイナリデータを用意します
BinaryData = b'abc' 

for i in ('md5','sha1'):
    # ハッシュオブジェクトを作ります
    h = hashlib.new( i)

    # バイナリデータからハッシュを計算します
    h.update(BinaryData)

    # ハッシュオブジェクトを16進数で出力します
    print( i, h.hexdigest())